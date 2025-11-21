"""Enumerations shared across models."""

from enum import Enum


class UserRole(str, Enum):
    """User roles available within the platform."""

    GUEST = "guest"
    USER = "user"
    ADMIN = "admin"


class QuestionType(str, Enum):
    """Supported question types."""

    SINGLE = "single"
    MULTI = "multi"


class ProgressStatus(str, Enum):
    """Progress state for a lecture."""

    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"


