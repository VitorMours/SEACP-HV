from pathlib import Path
from fastapi import UploadFile
import os
from datetime import datetime
import logging
logger = logging.getLogger(__name__)


def build_raw_image_folder() -> None:
    raw_path = Path(__file__).resolve().parent.parent / "files" / "raw"
    if raw_path.exists():
        logger.info("Diretorio de imagens cruas ja existe")
    else:
        try:
            raw_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Diretorio '{raw_path}' criado com sucesso!")
        except Exception as e:
            logger.info(f"Ocorreu um erro ao criar o diretório: {e}")

def build_processed_image_folder() -> None:
    processed_path = Path(__file__).resolve().parent.parent / "files" / "processed"
    if processed_path.exists():
        logger.info("Diretorio de imagens processadas ja existe")
    else:
        try:
            processed_path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Diretorio '{processed_path}' criado com sucesso!")
        except Exception as e:
            logger.info(f"Ocorreu um erro ao criar o diretório: {e}")

def build_file_structure() -> None:
    path = Path(__file__).resolve().parent.parent / "files" 
    if path.exists():
        logger.info("Diretorio de Files existe")
    else:
        try:
            path.mkdir(parents=True, exist_ok=True)
            logger.info(f"Diretório '{path}' criado com sucesso!")
        except Exception as e:
            logger.info(f"Ocorreu um erro ao criar o diretório: {e}")
            
    build_processed_image_folder()
    build_raw_image_folder()

def rename_image(image: UploadFile, name: str = None) -> str:
    """
    Método para renomear a imagem.
    Garante a preservação da extensão e sanitização do nome.
    """
    base_name, extension = os.path.splitext(image.filename)
    
    if name is None:
        file_new_name = base_name.replace(" ", "_").lower()
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        filename = f"{file_new_name}_{timestamp}{extension}"
        return filename
    else:
        return f"{name}{extension}"