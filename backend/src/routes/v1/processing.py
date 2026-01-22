from fastapi import APIRouter, File, status
from fastapi.responses import FileResponse, JSONResponse
from typing import Annotated, List
from services.image_processing_service import ImageProcessingService
import base64
import cv2
router = APIRouter(tags=["processamento"], prefix="/process")


@router.get("/")
async def index_processing():
  return {"Hello":"world"}


@router.get("/{filename}", status_code=status.HTTP_200_OK)
async def process_image(filename: str):
  try:
    np_array = ImageProcessingService.process_image(filename)
    if np_array is None:
      return JSONResponse(
        status_code=400,
        content={"success": False, "error": "Falha ao processar a imagem"}
      )
    
    # Codificar imagem em base64 (muito mais rápido que tolist())
    _, img_encoded = cv2.imencode('.jpg', np_array)
    img_base64 = base64.b64encode(img_encoded).decode('utf-8')
    
    return {
      "success": True,
      "image": img_base64,
      "shape": np_array.shape,
      "dtype": str(np_array.dtype)
    }
  except Exception as e:
    return JSONResponse(
      status_code=500,
      content={"success": False, "error": str(e)}
    )