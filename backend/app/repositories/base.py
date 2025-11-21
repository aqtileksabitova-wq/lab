"""Base repository abstraction."""

from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:
    """Stores the session reference and common helpers."""

    def __init__(self, session: AsyncSession):
        self.session = session


