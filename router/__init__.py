from fastapi import APIRouter

master_router = APIRouter(
    prefix="/api",
    tags=["master"]
)

from .file import file_route
master_router.include_router(file_route)