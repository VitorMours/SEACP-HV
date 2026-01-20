from fastapi import APIRouter, File, status
from fastapi.responses import FileResponse
from typing import Annotated, List

router = APIRouter(tags=["processamento"], prefix="/process")


@router.get("/")
async def index_processing():
  return {"Hello":"world"}


@router.get("/{filename}", status_code=status.HTTP_200_OK)
async def process_image(filename: str):
  pass
  