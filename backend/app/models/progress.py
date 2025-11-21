"""User progress model."""

from sqlalchemy import ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.session import Base
from app.models.enums import ProgressStatus


class UserProgress(Base):
    """Stores user progress per lecture."""

    __tablename__ = "user_progress"
    __table_args__ = (UniqueConstraint("user_id", "lecture_id", name="uq_user_lecture"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), nullable=False, index=True)
    lecture_id: Mapped[int] = mapped_column(ForeignKey("lectures.id", ondelete="CASCADE"), nullable=False, index=True)
    status: Mapped[ProgressStatus] = mapped_column(default=ProgressStatus.NOT_STARTED, nullable=False)

    user: Mapped["User"] = relationship(back_populates="progresses")
    lecture: Mapped["Lecture"] = relationship(back_populates="progresses")


