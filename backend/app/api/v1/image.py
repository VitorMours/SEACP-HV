from typing import List
from app.schemas.image import ImageRead, ImageCreate
from app.services.image import ImageProcessingService, ImageService
from fastapi import APIRouter, Depends, UploadFile, File

router = APIRouter(prefix="/images", tags=["Image"])


def get_image_service() -> ImageService:
  return ImageService()

def get_image_processing_service() -> ImageProcessingService:
  return ImageProcessingService()

@router.get("/", response_model = List[ImageRead])
async def get_all_images(service: ImageService = Depends(get_image_service)):
  return service.get_all_images_info()

@router.post("/") # , response_model = ImageCreate
async def update_image_in_system(file: UploadFile = File(...), service: ImageService = Depends(get_image_service)):
  return service.ingest_image(file)
  
