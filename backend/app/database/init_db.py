"""Database initialization and seeding logic."""

from copy import deepcopy

from sqlalchemy import select, func

from app.core.config import get_settings
from app.database.session import Base, async_engine, async_session_factory
from app.models.answer import Answer
from app.models.lecture import Lecture
from app.models.question import Question
from app.models.test import Test
from app.models.user import User
from app.models.enums import UserRole
from app.services.auth import get_password_hash
from app.seed.init_data import LECTURES, TESTS


settings = get_settings()


async def init_data():
    """Create database schema and seed initial data."""

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with async_session_factory() as session:
        lecture_count = await session.scalar(select(func.count(Lecture.id)))
        if lecture_count and lecture_count > 0:
            return

        lecture_entities = []
        for lecture_payload in LECTURES:
            lecture = Lecture(**lecture_payload)
            session.add(lecture)
            lecture_entities.append(lecture)
        await session.flush()

        for test_payload in TESTS:
            payload = deepcopy(test_payload)
            lecture_index = payload.pop("lecture_index")
            questions = payload.pop("questions", [])
            test = Test(lecture_id=lecture_entities[lecture_index].id, **payload)
            session.add(test)
            await session.flush()

            for question_payload in questions:
                answers = question_payload.pop("answers", [])
                question = Question(test_id=test.id, **question_payload)
                session.add(question)
                await session.flush()
                for answer_payload in answers:
                    answer = Answer(question_id=question.id, **answer_payload)
                    session.add(answer)

        await session.commit()

    await _ensure_default_admin()


async def _ensure_default_admin():
    async with async_session_factory() as session:
        existing = await session.scalar(select(User).where(User.email == settings.default_admin_email))
        if existing:
            return
        admin = User(
            email=settings.default_admin_email,
            password_hash=get_password_hash(settings.default_admin_password),
            role=UserRole.ADMIN,
        )
        session.add(admin)
        await session.commit()


