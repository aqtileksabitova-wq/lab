"""Test model definition."""

from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base


class Test(Base):
    """Represents a test related to a lecture."""

    __tablename__ = "tests"

    id: Mapped[int] = mapped_column(primary_key=True)
    lecture_id: Mapped[int] = mapped_column(ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str | None] = mapped_column(String(512))

    lecture: Mapped["Lecture"] = relationship(back_populates="tests")
    questions: Mapped[list["Question"]] = relationship(back_populates="test", cascade="all, delete-orphan")
    results: Mapped[list["TestResult"]] = relationship(back_populates="test", cascade="all, delete-orphan")


