"""Lecture repository."""

from sqlalchemy import select

from app.models.lecture import Lecture
from app.repositories.base import BaseRepository


class LectureRepository(BaseRepository):
    async def list(self) -> list[Lecture]:
        result = await self.session.execute(select(Lecture))
        return list(result.scalars().all())

    async def get(self, lecture_id: int) -> Lecture | None:
        result = await self.session.execute(select(Lecture).where(Lecture.id == lecture_id))
        return result.scalar_one_or_none()

    async def create(self, data: dict) -> Lecture:
        lecture = Lecture(**data)
        self.session.add(lecture)
        await self.session.flush()
        return lecture

    async def update(self, lecture: Lecture, data: dict) -> Lecture:
        for key, value in data.items():
            setattr(lecture, key, value)
        await self.session.flush()
        return lecture

    async def delete(self, lecture: Lecture) -> None:
        await self.session.delete(lecture)
        await self.session.flush()


