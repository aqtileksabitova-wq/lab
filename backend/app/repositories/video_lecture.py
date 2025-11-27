"""Video lecture repository."""

from sqlalchemy import select

from app.models.video_lecture import VideoLecture
from app.repositories.base import BaseRepository


class VideoLectureRepository(BaseRepository):
    async def list(self) -> list[VideoLecture]:
        result = await self.session.execute(select(VideoLecture).order_by(VideoLecture.created_at))
        return list(result.scalars().all())

    async def get_by_id(self, lecture_id: int) -> VideoLecture | None:
        result = await self.session.execute(select(VideoLecture).where(VideoLecture.id == lecture_id))
        return result.scalar_one_or_none()




