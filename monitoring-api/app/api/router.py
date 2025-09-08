from fastapi import APIRouter
from .endpoints import health
from .endpoints import services

router = APIRouter()

router.include_router(health, prefix="/api/health", tags=["Health Check"])
router.include_router(services, prefix="/api/services", tags=["Services"])
