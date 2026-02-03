from fastapi import APIRouter, File, Response, status
from fastapi.responses import FileResponse
from typing import Annotated, List
from services.image_processing_service import ImageProcessingService
router = APIRouter(tags=["processamento"], prefix="/process")

@router.get("/{filename}", status_code=status.HTTP_200_OK)
async def process_image(filename: str):
  np_array = ImageProcessingService.process_image(filename)
  return Response(content=np_array.tolist())

@router.get("/gray_scale/{filename}", status_code=status.HTTP_200_OK)
async def generate_gray_scale(filename: str):
  np_array = ImageProcessingService.process_image(filename)
  gray_img = ImageProcessingService.generate_gray_scale_image_version(np_array)
  return Response(content=gray_img, media_type="image/jpeg")
