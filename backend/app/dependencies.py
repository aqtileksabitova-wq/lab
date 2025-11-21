"""Reusable FastAPI dependencies."""

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.ext.asyncio import AsyncSession

from app.database.session import get_db
from app.models.enums import UserRole
from app.repositories.user import UserRepository
from app.schemas.user import TokenPayload
from app.services.auth import decode_token


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme), db: AsyncSession = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    payload = decode_token(token)
    if payload is None:
        raise credentials_exception
    token_data = TokenPayload(**payload)
    if token_data.sub is None:
        raise credentials_exception

    repo = UserRepository(db)
    user = await repo.get_by_email(token_data.sub)
    if user is None:
        raise credentials_exception
    return user


async def get_current_admin(user=Depends(get_current_user)):
    if user.role != UserRole.ADMIN:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Admin privileges required")
    return user


