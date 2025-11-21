# Платформа для изучения C++

Полноценный стартовый шаблон веб-платформы из ТЗ: FastAPI + React (Vite) + SQLite/PostgreSQL-ready.

## Быстрый запуск
```bash
# Backend
cd backend
python -m venv .venv && .venv\Scripts\activate
pip install -r requirements.txt
cp env.example .env
uvicorn app.main:app --reload

# Frontend
cd ../frontend
npm install
npm run dev
```

## Функциональные модули
- Регистрация/авторизация (JWT, bcrypt)
- Роли: пользователь и админ (гостевой доступ к лекциям)
- Лекции и тесты (3 лекции + 3 теста загружаются автоматически)
- Прохождение теста с мгновенной проверкой и сохранением результата
- Прогресс пользователя и история попыток
- Админ-панель для создания лекций и тестов

## Технологии
- **Backend**: FastAPI, SQLAlchemy 2.0, Pydantic v2, Alembic
- **Frontend**: React 18 + Vite + TailwindCSS + Zustand
- **БД**: SQLite по умолчанию, совместимость с PostgreSQL

## Структура
```
backend/
  app/        # FastAPI приложение
  seed/       # JSON-like данные для инициализации
  alembic/    # миграции
frontend/
  src/        # React клиент
```

## ENV
- `SECRET_KEY` — JWT ключ
- `DATABASE_URL` — строка подключения (sqlite+aiosqlite:///./db.sqlite3)
- `FRONTEND_URL` — CORS
- `DEFAULT_ADMIN_EMAIL` / `DEFAULT_ADMIN_PASSWORD` — авто-создаваемый админ
- `VITE_API_URL` — адрес API для клиента

