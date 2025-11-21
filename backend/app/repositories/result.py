"""Repository for test results."""

from sqlalchemy import select

from app.models.test_result import TestResult
from app.repositories.base import BaseRepository


class ResultRepository(BaseRepository):
    async def list_for_user(self, user_id: int) -> list[TestResult]:
        result = await self.session.execute(select(TestResult).where(TestResult.user_id == user_id))
        return list(result.scalars().all())

    async def create(self, user_id: int, test_id: int, score: int, total: int) -> TestResult:
        result = TestResult(user_id=user_id, test_id=test_id, score=score, total=total)
        self.session.add(result)
        await self.session.flush()
        return result


