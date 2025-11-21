"""Repository for user operations."""

from sqlalchemy import select, update
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User
from app.models.enums import UserRole
from app.repositories.base import BaseRepository


class UserRepository(BaseRepository):
    """Data access for users."""

    def __init__(self, session: AsyncSession):
        super().__init__(session)

    async def get_by_email(self, email: str) -> User | None:
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def get(self, user_id: int) -> User | None:
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def create(self, email: str, password_hash: str, role: UserRole = UserRole.USER) -> User:
        user = User(email=email, password_hash=password_hash, role=role)
        self.session.add(user)
        await self.session.flush()
        return user

    async def list_all(self) -> list[User]:
        result = await self.session.execute(select(User))
        return list(result.scalars().all())

    async def update_role(self, user_id: int, role: UserRole) -> User | None:
        await self.session.execute(update(User).where(User.id == user_id).values(role=role))
        await self.session.flush()
        return await self.get(user_id)


