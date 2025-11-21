"""Progress schemas."""

from pydantic import BaseModel, ConfigDict

from app.models.enums import ProgressStatus


class ProgressRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    user_id: int
    lecture_id: int
    status: ProgressStatus


class ProgressUpdate(BaseModel):
    lecture_id: int
    status: ProgressStatus


class ProgressSummary(BaseModel):
    completed: int
    total_lectures: int
    completion_rate: float


