"""Repositories for tests, questions, and answers."""

from sqlalchemy import select
from sqlalchemy.orm import selectinload

from app.models.answer import Answer
from app.models.question import Question
from app.models.test import Test
from app.repositories.base import BaseRepository


class TestRepository(BaseRepository):
    async def list_for_lecture(self, lecture_id: int) -> list[Test]:
        result = await self.session.execute(
            select(Test)
            .options(selectinload(Test.questions).selectinload(Question.answers))
            .where(Test.lecture_id == lecture_id)
        )
        return list(result.scalars().unique().all())

    async def get(self, test_id: int) -> Test | None:
        result = await self.session.execute(
            select(Test)
                .options(selectinload(Test.questions).selectinload(Question.answers))
                .where(Test.id == test_id)
        )
        return result.scalar_one_or_none()

    async def create(self, data: dict) -> Test:
        questions_data = data.pop("questions", [])
        test = Test(**data)
        self.session.add(test)
        await self.session.flush()
        await self._upsert_questions(test, questions_data)
        await self.session.flush()
        return test

    async def update(self, test: Test, data: dict) -> Test:
        questions_data = data.pop("questions", None)
        for key, value in data.items():
            setattr(test, key, value)
        if questions_data is not None:
            await self._replace_questions(test, questions_data)
        await self.session.flush()
        return test

    async def delete(self, test: Test) -> None:
        await self.session.delete(test)
        await self.session.flush()

    async def _upsert_questions(self, test: Test, questions_data: list[dict]) -> None:
        for question_data in questions_data:
            answers_data = question_data.pop("answers", [])
            question = Question(test_id=test.id, **question_data)
            self.session.add(question)
            await self.session.flush()
            for answer_data in answers_data:
                answer = Answer(question_id=question.id, **answer_data)
                self.session.add(answer)

    async def _replace_questions(self, test: Test, questions_data: list[dict]) -> None:
        # delete existing
        for question in list(test.questions):
            await self.session.delete(question)
        await self.session.flush()
        await self._upsert_questions(test, questions_data)


