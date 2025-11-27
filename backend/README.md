# Backend – C++ Learning Platform

## Quick start
1. Create virtual env and install deps:
   ```bash
   cd backend
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```
2. Copy env template:
   ```bash
   cp env.example .env
   ```
3. Run API (auto seeds 10 лекций, 4 видеолекции и тесты):
   ```bash
   uvicorn app.main:app --reload
   ```

## Tech stack
- FastAPI + SQLAlchemy 2.0 + Pydantic v2
- Async DB driver (SQLite by default) with repository layer to switch to PostgreSQL
- Alembic migrations (run `alembic revision --autogenerate -m "..."` then `alembic upgrade head`)
- JWT auth, bcrypt hashing, admin guards
- Локальный C++ компилятор (ищется `g++` или `clang++`) для API `/compiler/run`
- При первом запуске создаётся админ `admin@cpp.local` / `ChangeMe123!` (меняется в `.env`)

## Structure
```
app/
  core/         # settings, security
  database/     # session + init
  models/       # SQLAlchemy models
  repositories/ # DB access layer
  routers/      # FastAPI routers
  schemas/      # Pydantic models
seed/           # initial lectures/tests data
alembic/        # migrations
```

## New endpoints
- `GET /video-lectures` – список видеолекций с YouTube
- `POST /compiler/run` – компиляция и запуск C++17/20 с ограничениями по времени


