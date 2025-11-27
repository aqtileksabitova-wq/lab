"""VideoLecture model definition."""

from datetime import datetime

from sqlalchemy import Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.session import Base


class VideoLecture(Base):
    """Represents an external video lecture hosted on YouTube."""

    __tablename__ = "video_lectures"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    short_description: Mapped[str] = mapped_column(String(512), nullable=False)
    youtube_id: Mapped[str] = mapped_column(String(32), unique=True, nullable=False)
    channel: Mapped[str] = mapped_column(String(128), nullable=False)
    duration_minutes: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now(), onupdate=func.now())




