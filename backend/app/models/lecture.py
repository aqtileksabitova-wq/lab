"""Lecture model definition."""

from datetime import datetime

from sqlalchemy import Text, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base


class Lecture(Base):
    """Represents a single lecture."""

    __tablename__ = "lectures"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    short_description: Mapped[str] = mapped_column(String(512), nullable=False)
    content: Mapped[str] = mapped_column(Text, nullable=False)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())

    tests: Mapped[list["Test"]] = relationship(back_populates="lecture", cascade="all, delete-orphan")
    progresses: Mapped[list["UserProgress"]] = relationship(back_populates="lecture", cascade="all, delete-orphan")


