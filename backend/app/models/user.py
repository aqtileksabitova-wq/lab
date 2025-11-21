"""User model."""

from datetime import datetime

from sqlalchemy import String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base
from app.models.enums import UserRole


class User(Base):
    """Represents a platform user."""

    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, nullable=False, index=True)
    password_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    role: Mapped[UserRole] = mapped_column(default=UserRole.USER, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    progresses: Mapped[list["UserProgress"]] = relationship(back_populates="user", cascade="all, delete-orphan")
    test_results: Mapped[list["TestResult"]] = relationship(back_populates="user", cascade="all, delete-orphan")


