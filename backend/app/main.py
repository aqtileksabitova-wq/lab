from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import get_settings
from app.database.init_db import init_data
from app.routers import auth, lectures, tests, users, progress

settings = get_settings()
app = FastAPI(title=settings.app_name, version=settings.app_version)

@app.on_event("startup")
async def on_startup():
    await init_data()

app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(auth.router)
app.include_router(lectures.router)
app.include_router(tests.router)
app.include_router(users.router)
app.include_router(progress.router)

@app.get("/")
async def healthcheck():
    return {"status": "ok", "service": settings.app_name}