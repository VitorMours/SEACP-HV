from fastapi import APIRouter
from .images import router as image_router

router = APIRouter(prefix="/v1")


router.include_router(image_router)