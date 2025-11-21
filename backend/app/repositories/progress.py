"""Repository for user progress."""

from sqlalchemy import select

from app.models.progress import UserProgress
from app.repositories.base import BaseRepository


class ProgressRepository(BaseRepository):
    async def get_progress(self, user_id: int) -> list[UserProgress]:
        result = await self.session.execute(select(UserProgress).where(UserProgress.user_id == user_id))
        return list(result.scalars().all())

    async def upsert(self, user_id: int, lecture_id: int, status) -> UserProgress:
        result = await self.session.execute(
            select(UserProgress).where(
                UserProgress.user_id == user_id,
                UserProgress.lecture_id == lecture_id,
            )
        )
        progress = result.scalar_one_or_none()
        if progress:
            progress.status = status
        else:
            progress = UserProgress(user_id=user_id, lecture_id=lecture_id, status=status)
            self.session.add(progress)
        await self.session.flush()
        return progress

    async def list_all(self) -> list[UserProgress]:
        result = await self.session.execute(select(UserProgress))
        return list(result.scalars().all())


