"""Lecture schemas."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class LectureBase(BaseModel):
    title: str
    short_description: str
    content: str


class LectureCreate(LectureBase):
    pass


class LectureUpdate(BaseModel):
    title: str | None = None
    short_description: str | None = None
    content: str | None = None


class LectureRead(LectureBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    created_at: datetime
    updated_at: datetime | None = None


