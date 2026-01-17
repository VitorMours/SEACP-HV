from services.image_service import ImageService
from fastapi import APIRouter, File, UploadFile
from typing import Annotated
from pathlib import Path
import shutil
router = APIRouter(tags=["processamento"], prefix="/images")


@router.get("/")
async def get_all_images():
    return {"getting_all": "images"}

@router.post("/")
async def uploading_image(file: Annotated[UploadFile, File(...)]):
    try:
        files_path = Path(__file__).resolve().parent.parent.parent / "files"
        
        file_location = ImageService.ingest_image_in_server(files_path, file)        
        
        return {
            "success": True,
            "filename": file.filename,
            "content_type": file.content_type,
            "location": str(file_location)
        }
    except Exception as e:
        return {"success": False, "error": f"{e}"}
    finally: 
        await file.close()


