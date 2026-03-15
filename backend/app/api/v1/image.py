import logging
from typing import List
from app.workers.image import process_image_to_histogram_analysis
from app.schemas.image import ImageRead, ImageCreate
from app.services.image import ImageService
from app.services.image_processing import ImageProcessingService
from app.models import get_session
from app.repository.image_repository import ImageRepository
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Response
from sqlmodel import Session
from app.core.logging import get_logger

logger = get_logger(__name__)

def get_image_repository(session: Session = Depends(get_session)) -> ImageRepository:
    return ImageRepository(session)

def get_image_service(repository: ImageRepository = Depends(get_image_repository)) -> ImageService:
    return ImageService(repository)

def get_image_processing_service() -> ImageProcessingService:
  return ImageProcessingService()

router = APIRouter(prefix="/images", tags=["Image"])

@router.get("/", response_model = List[ImageRead])
async def get_all_images(service: ImageService = Depends(get_image_service)):
  logger.info("[ROUTER] Fetching all images")
  return service.return_all_images()

@router.post("/", response_model = ImageCreate)
async def update_image_in_system(file: UploadFile = File(...), image_service: ImageService = Depends(get_image_service)):
  logger.info("[ROUTER] Updating an image")
  image = image_service.ingest_image(file)
  process_image_to_histogram_analysis.delay(image.id)
  
  return image

@router.get("/{image_id}", response_model = ImageRead)
async def get_image_by_id(image_id: int, image_service: ImageService = Depends(get_image_service)):
  logger.info("[ROUTER] Getting image by the database id")
  try:
    return image_service.return_image_by_id(image_id)
  except ValueError as e:
    raise HTTPException(status_code=404, detail=str(e))

@router.get("/process/{image_id}")
async def processed_image_by_id(image_id: int, image_service = Depends(get_image_service), processing_service = Depends(get_image_processing_service)):
  logger.info("[ROUTER] Solicitando processamento de imagem")
  result: ImageRead = image_service.return_image_by_id(image_id)
  array = processing_service.process_image(result)
  return Response(
        content=array.tobytes(),
        media_type="image/png"
    )

@router.get("/process/{image_id}/grayscale")
async def processed_image_by_id_as_grayscale(image_id: int, image_service = Depends(get_image_service), processing_service = Depends(get_image_processing_service)):
  logger.info("[ROUTER] Solicitando processamento da imagem para escala de cinza")
  result: ImageRead = image_service.return_image_by_id(image_id)
  array = processing_service.convert_image_to_grayscale(result)
  return Response(
        content=array.tobytes(),
        media_type="image/png"
    )
  