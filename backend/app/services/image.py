import glob
import os
from app.repository.image_repository import ImageRepository
from app.models.image import Image
import cv2
import numpy as np
from pathlib import Path
from app.core.config import config
from app.schemas.image import ImageRead, ImageCreate
from fastapi import File
from sqlmodel import Session
import shutil
import base64

class ImageService:
  """
  Classe para trabalhar com a ingestao, verificacao, leitura
  e manuseio de arquivos audiovisuais dentro do sistema, de forma
  a fornecer acesso original aos arquivos enviados, e de forma a fornecer
  a outros sistemas, os arquivos do usuario de forma que sejam
  processados com o intuito de gerar informacao e conhecimento
  """

  def __init__(self, repository: ImageRepository) -> None:
    self.repository = repository
    self.raw_image_path = config.raw_image_dir
    self.processed_image_path = config.processed_image_dir

  def ingest_image(self, file: File) -> ImageCreate:
    with open(f"{self.raw_image_path}/{file.filename}", "wb") as buffer:
      shutil.copyfileobj(file.file, buffer)
    filetype = Path(file.filename).suffix.replace(".", "")

    new_image = Image(name=file.filename, was_processed=False, path=str(Path(file.filename)))
    self.repository.save_image(new_image)
    
    return ImageCreate(image_name=file.filename, filetype=filetype)

  def return_all_images(self) -> list[Path]:
    images = list()
    for filename in os.listdir(self.raw_image_path):
      if filename.endswith((".jpg",".jpeg",".png",".webp")):
        full_path = os.path.join(self.raw_image_path, filename)
        
        with open(full_path, "rb") as f:
          image_bytes = f.read()
        new_image = ImageRead(
          image = base64.b64encode(image_bytes).decode("utf-8"),
          image_name=filename,
          filetype=filename.split(".")[-1],
          path=full_path
        )
        images.append(new_image)
    return images
  
  def return_image_by_id(self, id: int) -> ImageRead:
    image = self.repository.fetch_image_by_id(id)
    
    if image is None:
        raise ValueError(f"Imagem com id {id} não encontrada")
    
    full_path = os.path.join(self.raw_image_path, image.name)
    
    with open(full_path, "rb") as f:
        image_bytes = f.read()
    
    return ImageRead(
        image=base64.b64encode(image_bytes).decode("utf-8"),
        image_name=image.name,
        filetype=image.name.split(".")[-1],
        path=full_path
    )
   