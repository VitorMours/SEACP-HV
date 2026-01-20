from fastapi import APIRouter
from .images import router as image_router
from .processing import router as process_router

router = APIRouter(prefix="/v1")

router.include_router(image_router)
router.include_router(process_router)