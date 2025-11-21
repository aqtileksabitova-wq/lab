"""User-focused endpoints: progress, results, profile."""

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.dependencies import get_current_admin, get_current_user
from app.models.enums import ProgressStatus
from app.repositories.progress import ProgressRepository
from app.repositories.result import ResultRepository
from app.schemas.progress import ProgressRead, ProgressSummary
from app.schemas.result import ResultRead


router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me/progress", response_model=list[ProgressRead])
async def my_progress(current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    repo = ProgressRepository(db)
    return await repo.get_progress(current_user.id)


@router.get("/me/results", response_model=list[ResultRead])
async def my_results(current_user=Depends(get_current_user), db: AsyncSession = Depends(get_db)):
    repo = ResultRepository(db)
    return await repo.list_for_user(current_user.id)


@router.get("/stats/summary", response_model=ProgressSummary)
async def progress_summary(db: AsyncSession = Depends(get_db), _: int = Depends(get_current_admin)):
    repo = ProgressRepository(db)
    all_progress = await repo.list_all()
    completed = sum(1 for item in all_progress if item.status == ProgressStatus.COMPLETED)
    lecture_ids = {item.lecture_id for item in all_progress}
    total_lectures = len(lecture_ids)
    completion_rate = completed / total_lectures if total_lectures else 0.0
    return ProgressSummary(completed=completed, total_lectures=total_lectures, completion_rate=completion_rate)


