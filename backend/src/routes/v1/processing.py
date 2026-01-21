from fastapi import APIRouter, File, status
from fastapi.responses import FileResponse
from typing import Annotated, List
from services.image_processing_service import ImageProcessingService
router = APIRouter(tags=["processamento"], prefix="/process")


@router.get("/")
async def index_processing():
  return {"Hello":"world"}


@router.get("/{filename}", status_code=status.HTTP_200_OK)
async def process_image(filename: str):
  np_array = ImageProcessingService.process_image(filename)
  return {"sucess": True, "img_array":np_array}