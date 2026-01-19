import mimetypes
from schemas.image_schema import ImageRequest, ImageResponse
from services.image_service import ImageService
from fastapi import APIRouter, File, UploadFile, status
from fastapi.responses import FileResponse
from typing import Annotated, List
from pathlib import Path
import os

router = APIRouter(tags=["processamento"], prefix="/images")

@router.get("/", response_model=List[ImageRequest], status_code = status.HTTP_200_OK)
async def get_all_images():
    try:
        files_path = Path(__file__).resolve().parent.parent.parent / "files" / "raw"
        files_list = []
        if files_path.exists():
            for item in files_path.iterdir():
                if item.is_file():
                    mime_type, _ = mimetypes.guess_type(item.name)
                    image = ImageRequest(
                        name = item.name,
                        mimetype = mime_type or "application/octet-stream",
                        filepath = str(item)
                    )
                    files_list.append(image)
        return files_list
        
    except Exception as e:
        return {"success": False, "error": f"{e}"}


@router.get("/{filename}", status_code = status.HTTP_200_OK)
async def download_image(filename: str):
    try:
        files_path = Path(__file__).resolve().parent.parent.parent / "files" / "processed" / filename
        if not files_path.exists():
            return {"success": False, "error": "Arquivo não encontrado"}
        return FileResponse(path=files_path, media_type="application/octet-stream", filename=filename)
    except Exception as e:
        return {"success": False, "error": f"{e}"}

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




