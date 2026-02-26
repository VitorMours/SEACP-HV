from typing import List
from schemas.image import ImageRead
from services.image import ImageProcessingService, ImageService
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/images", tags=["Image"])


def get_image_service() -> ImageService:
  return ImageService()

def get_image_processing_service() -> ImageProcessingService:
  return ImageProcessingService()

@router.get("/", response_model = List[ImageRead])
async def get_all_images(service: ImageService = Depends(get_image_service)):
  return service.get_all_images_info()
  
