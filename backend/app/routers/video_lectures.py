"""Video lecture endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.repositories.video_lecture import VideoLectureRepository
from app.schemas.video_lecture import VideoLectureRead

router = APIRouter(prefix="/video-lectures", tags=["video-lectures"])


@router.get("", response_model=list[VideoLectureRead])
async def list_video_lectures(db: AsyncSession = Depends(get_db)):
    repo = VideoLectureRepository(db)
    return await repo.list()




