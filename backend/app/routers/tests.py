"""Test and quiz endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.dependencies import get_current_admin, get_current_user
from app.models.enums import ProgressStatus
from app.repositories.progress import ProgressRepository
from app.repositories.result import ResultRepository
from app.repositories.test import TestRepository
from app.schemas.result import ResultRead
from app.schemas.test import TestCreate, TestRead, TestSubmission, TestUpdate


router = APIRouter(prefix="/tests", tags=["tests"])


@router.get("/{test_id}", response_model=TestRead)
async def get_test(test_id: int, db: AsyncSession = Depends(get_db), _: int = Depends(get_current_user)):
    repo = TestRepository(db)
    test = await repo.get(test_id)
    if test is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test not found")
    return test


@router.post("", response_model=TestRead, status_code=status.HTTP_201_CREATED)
async def create_test(payload: TestCreate, db: AsyncSession = Depends(get_db), _: int = Depends(get_current_admin)):
    repo = TestRepository(db)
    test = await repo.create(payload.model_dump())
    await db.commit()
    await db.refresh(test)
    return test


@router.put("/{test_id}", response_model=TestRead)
async def update_test(
    test_id: int,
    payload: TestUpdate,
    db: AsyncSession = Depends(get_db),
    _: int = Depends(get_current_admin),
):
    repo = TestRepository(db)
    test = await repo.get(test_id)
    if test is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test not found")
    test = await repo.update(test, payload.model_dump(exclude_unset=True))
    await db.commit()
    await db.refresh(test)
    return test


@router.delete("/{test_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_test(test_id: int, db: AsyncSession = Depends(get_db), _: int = Depends(get_current_admin)):
    repo = TestRepository(db)
    test = await repo.get(test_id)
    if test is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test not found")
    await repo.delete(test)
    await db.commit()
    return None


@router.post("/{test_id}/submit", response_model=ResultRead)
async def submit_test(
    test_id: int,
    payload: TestSubmission,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user),
):
    repo = TestRepository(db)
    test = await repo.get(test_id)
    if test is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Test not found")

    score = 0
    answers_map = {item.question_id: set(item.selected_answer_ids) for item in payload.answers}

    for question in test.questions:
        correct_ids = {answer.id for answer in question.answers if answer.is_correct}
        selected_ids = answers_map.get(question.id, set())
        if correct_ids == set(selected_ids):
            score += 1

    result_repo = ResultRepository(db)
    progress_repo = ProgressRepository(db)
    result = await result_repo.create(current_user.id, test_id, score=score, total=len(test.questions))

    status_value = ProgressStatus.COMPLETED if score == len(test.questions) else ProgressStatus.IN_PROGRESS
    await progress_repo.upsert(current_user.id, test.lecture_id, status_value)

    await db.commit()
    await db.refresh(result)

    return result


