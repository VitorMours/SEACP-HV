from schemas.image_schema import ImageResponse
from services.image_service import ImageService
from fastapi import APIRouter, File, UploadFile, status
from typing import Annotated
from pathlib import Path
router = APIRouter(tags=["processamento"], prefix="/images")


@router.get("/")
async def get_all_images():
    return {"getting_all": "images"}

@router.post("/", response_model = ImageResponse, status_code = status.HTTP_201_CREATED)
async def uploading_image(file: Annotated[UploadFile, File(...)]):
    try:
        files_path = Path(__file__).resolve().parent.parent.parent / "files" / "raw"
        response = ImageService.ingest_image_in_server(files_path, file)        
        return response
       
    except Exception as e:
        return {"success": False, "error": f"{e}"}
    finally: 
        await file.close()


