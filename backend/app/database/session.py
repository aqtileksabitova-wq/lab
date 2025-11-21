"""Database engine, session factory, and base declarative class."""

from collections.abc import Generator
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Session
from sqlalchemy import create_engine

from app.core.config import get_settings


settings = get_settings()


def _resolve_async_url(url: str) -> str:
    """Ensure SQLite URLs use the async driver."""

    if url.startswith("sqlite") and "aiosqlite" not in url:
        return url.replace("sqlite:///", "sqlite+aiosqlite:///")
    return url


def _resolve_sync_url(url: str) -> str:
    """Return sync driver variant of DB URL (used for Alembic/seed tasks)."""

    if url.startswith("sqlite+aiosqlite"):
        return url.replace("sqlite+aiosqlite:///", "sqlite:///")
    return url


ASYNC_DATABASE_URL = _resolve_async_url(settings.database_url)
SYNC_DATABASE_URL = _resolve_sync_url(settings.database_url)

async_engine = create_async_engine(ASYNC_DATABASE_URL, future=True)
sync_engine = create_engine(SYNC_DATABASE_URL, future=True)


class Base(DeclarativeBase):
    """Base declarative class for all models."""

    pass


async_session_factory = async_sessionmaker(async_engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Yield an async session for FastAPI dependencies."""

    async with async_session_factory() as session:
        yield session


def get_sync_session() -> Generator[Session, None, None]:
    """Yield a sync session (useful for scripts/seeding)."""

    with Session(sync_engine) as session:
        yield session


