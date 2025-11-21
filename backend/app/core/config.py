"""Application configuration and settings."""

from functools import lru_cache
from pathlib import Path

from pydantic import AnyHttpUrl, EmailStr, Field, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    """Application settings loaded from environment variables or defaults."""

    model_config = SettingsConfigDict(env_file=str(BASE_DIR.parent / ".env"), env_file_encoding="utf-8")

    app_name: str = "CppLearn"
    app_version: str = "0.1.0"
    secret_key: str = Field("change-me-change-me", min_length=16)
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60 * 24
    database_url: str = Field(
        default="sqlite+aiosqlite:///./db.sqlite3",
        description="SQLAlchemy database URL (SQLite by default).",
    )
    frontend_url: AnyHttpUrl | None = Field(
        default="http://localhost:5173",
        description="Allowed CORS origin for production.",
    )
    default_admin_email: EmailStr = Field(default="admin@example.com")
    default_admin_password: str = Field(default="ChangeMe123!")

    @field_validator("secret_key", mode="before")
    @classmethod
    def ensure_secret_key(cls, value: str) -> str:
        if isinstance(value, str) and len(value) >= 16:
            return value
        return "change-me-change-me"

    @field_validator("default_admin_email", mode="before")
    @classmethod
    def ensure_admin_email(cls, value: str) -> str:
        try:
            EmailStr(value)
            return value
        except Exception:
            return "admin@example.com"


@lru_cache
def get_settings() -> Settings:
    """Return cached settings instance."""

    return Settings()


