from contextlib import asynccontextmanager
from fastapi import FastAPI
from .api.router import router
from .db.session import db

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up...")
    await db.init_db()
    yield
    print("Shutting down...")
    await db.close_db()

app=FastAPI(
    title="Internal API Monitoring System",
    description="API for monitoring internal services",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(router)

