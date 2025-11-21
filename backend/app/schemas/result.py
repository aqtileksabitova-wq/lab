"""Schemas for reporting test results and history."""

from datetime import datetime

from pydantic import BaseModel, ConfigDict


class ResultRead(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    test_id: int
    score: int
    total: int
    passed_at: datetime


