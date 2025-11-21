"""Progress endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.dependencies import get_current_admin, get_current_user
from app.repositories.progress import ProgressRepository
from app.schemas.progress import ProgressRead, ProgressUpdate


router = APIRouter(prefix="/progress", tags=["progress"])


@router.post("/update", response_model=ProgressRead)
async def update_progress(
    payload: ProgressUpdate,
    current_user=Depends(get_current_user),
    db: AsyncSession = Depends(get_db),
):
    repo = ProgressRepository(db)
    progress = await repo.upsert(current_user.id, payload.lecture_id, payload.status)
    await db.commit()
    await db.refresh(progress)
    return ProgressRead(lecture_id=progress.lecture_id, status=progress.status)


@router.get("/all", response_model=list[ProgressRead])
async def list_all_progress(db: AsyncSession = Depends(get_db), _: int = Depends(get_current_admin)):
    repo = ProgressRepository(db)
    return await repo.list_all()


