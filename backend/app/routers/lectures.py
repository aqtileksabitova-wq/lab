"""Lecture endpoints."""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.dependencies import get_current_admin, get_current_user
from app.repositories.lecture import LectureRepository
from app.repositories.test import TestRepository
from app.schemas.lecture import LectureCreate, LectureRead, LectureUpdate
from app.schemas.test import TestRead


router = APIRouter(prefix="/lectures", tags=["lectures"])


@router.get("", response_model=list[LectureRead])
async def list_lectures(db: AsyncSession = Depends(get_db)):
    repo = LectureRepository(db)
    lectures = await repo.list()
    return lectures


@router.get("/{lecture_id}", response_model=LectureRead)
async def get_lecture(lecture_id: int, db: AsyncSession = Depends(get_db)):
    repo = LectureRepository(db)
    lecture = await repo.get(lecture_id)
    if lecture is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecture not found")
    return lecture


@router.get("/{lecture_id}/tests", response_model=list[TestRead])
async def get_lecture_tests(lecture_id: int, db: AsyncSession = Depends(get_db)):
    repo = TestRepository(db)
    tests = await repo.list_for_lecture(lecture_id)
    return tests


@router.post("", response_model=LectureRead, status_code=status.HTTP_201_CREATED)
async def create_lecture(
    payload: LectureCreate,
    db: AsyncSession = Depends(get_db),
    _: int = Depends(get_current_admin),
):
    repo = LectureRepository(db)
    lecture = await repo.create(payload.model_dump())
    await db.commit()
    await db.refresh(lecture)
    return lecture


@router.put("/{lecture_id}", response_model=LectureRead)
async def update_lecture(
    lecture_id: int,
    payload: LectureUpdate,
    db: AsyncSession = Depends(get_db),
    _: int = Depends(get_current_admin),
):
    repo = LectureRepository(db)
    lecture = await repo.get(lecture_id)
    if lecture is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecture not found")
    lecture = await repo.update(lecture, payload.model_dump(exclude_unset=True))
    await db.commit()
    await db.refresh(lecture)
    return lecture


@router.delete("/{lecture_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_lecture(
    lecture_id: int,
    db: AsyncSession = Depends(get_db),
    _: int = Depends(get_current_admin),
):
    repo = LectureRepository(db)
    lecture = await repo.get(lecture_id)
    if lecture is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lecture not found")
    await repo.delete(lecture)
    await db.commit()
    return None


