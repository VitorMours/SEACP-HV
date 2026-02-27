
import cv2
import numpy as np
from pathlib import Path
from app.core.config import config
from app.schemas.image import ImageRead, ImageCreate
from fastapi import File
import shutil

class ImageService:
  """
  Classe para trabalhar com a ingestao, verificacao, leitura
  e manuseio de arquivos audiovisuais dentro do sistema, de forma
  a fornecer acesso original aos arquivos enviados, e de forma a fornecer
  a outros sistemas, os arquivos do usuario de forma que sejam
  processados com o intuito de gerar informacao e conhecimento
  """

  def __init__(self) -> None:
    self.raw_image_path = config.raw_image_dir
    self.processed_image_path = config.processed_image_dir

  def ingest_image(self, file: File) -> ImageCreate:
    with open(f"{self.raw_image_path}/{file.filename}", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    filetype = Path(file.filename).suffix.replace(".", "")

    return ImageCreate(
        image_name=file.filename,
        filetype=filetype
    )






class ImageProcessingService:


  @staticmethod
  def convert_image_to_grayscale() -> None:
    pass
