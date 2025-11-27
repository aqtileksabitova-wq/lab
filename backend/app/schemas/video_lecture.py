"""Pydantic schemas for video lectures."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class VideoLectureRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    short_description: str
    youtube_id: str
    channel: str
    duration_minutes: int
    created_at: datetime
    updated_at: datetime | None = None




