"""Database initialization and seeding logic."""

from copy import deepcopy

from sqlalchemy import func, select

from app.core.config import get_settings
from app.database.session import Base, async_engine, async_session_factory
from app.models.answer import Answer
from app.models.enums import UserRole
from app.models.lecture import Lecture
from app.models.question import Question
from app.models.test import Test
from app.models.user import User
from app.models.video_lecture import VideoLecture
from app.seed.init_data import LECTURES, TESTS, VIDEO_LECTURES
from app.services.auth import get_password_hash

settings = get_settings()


async def init_data():
    """Create database schema and seed initial data."""

    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    await _seed_learning_content()
    await _ensure_default_admin()


async def _seed_learning_content():
    async with async_session_factory() as session:
        lectures_by_title: dict[str, Lecture] = {}
        for lecture_payload in LECTURES:
            lecture = await session.scalar(select(Lecture).where(Lecture.title == lecture_payload["title"]))
            if lecture is None:
                lecture = Lecture(**lecture_payload)
                session.add(lecture)
                await session.flush()
            lectures_by_title[lecture.title] = lecture

        # Создаём тесты для всех лекций, если их ещё нет
        for test_payload in TESTS:
            payload = deepcopy(test_payload)
            lecture_title = payload.pop("lecture_title")
            questions = payload.pop("questions", [])
            lecture = lectures_by_title.get(lecture_title)
            if lecture is None:
                continue
            
            # Проверяем, есть ли уже тест для этой лекции
            existing_test = await session.scalar(
                select(Test).where(Test.lecture_id == lecture.id)
            )
            if existing_test:
                continue  # Тест уже существует, пропускаем
            
            # Создаём новый тест
            test = Test(lecture_id=lecture.id, **payload)
            session.add(test)
            await session.flush()

            # Добавляем вопросы и ответы
            for question_payload in questions:
                answers = question_payload.pop("answers", [])
                question = Question(test_id=test.id, **question_payload)
                session.add(question)
                await session.flush()
                for answer_payload in answers:
                    answer = Answer(question_id=question.id, **answer_payload)
                    session.add(answer)

        for video_payload in VIDEO_LECTURES:
            existing_video = await session.scalar(
                select(VideoLecture).where(VideoLecture.youtube_id == video_payload["youtube_id"])
            )
            if existing_video:
                continue
            session.add(VideoLecture(**video_payload))

        await session.commit()


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


