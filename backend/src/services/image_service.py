from utils.image_utils import rename_image
from schemas.image_schema import ImageResponse
from fastapi import File
import shutil
from pathlib import Path
import pandas as pd 
import numpy as np 
import logging

logger = logging.getLogger(__name__)

class ImageService:
    
    @staticmethod
    def ingest_image_in_server(file_directory_path: str, file: File) -> ImageResponse:
        try:
            new_filename = rename_image(file)
            file_location = file_directory_path / new_filename
            
            logger.info(f"Processando arquivo: {file.filename}")
            logger.info(f"Diretório destino: {file_directory_path}")
            logger.info(f"Novo nome do arquivo: {new_filename}")

            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)

            logger.info(f"Arquivo salvo com sucesso em: {file_location}")

            response = ImageResponse(
                name = f"{new_filename}",
                mimetype = file.content_type,
                filepath = str(file_location),
                success=True
            )

            logger.info(f"Resposta criada: {response}")

            return response

        except Exception:
            return ImageResponse(
                name="",
                mimetype=file.content_type if hasattr(file, 'content_type') else "",
                filepath="",
                success=False
            )
            
    @staticmethod 
    def process_image() -> None:
        pass