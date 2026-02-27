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
      
class ImageProcessingService:
  """
  Servico focado no processamento de imagens e nas transfomacoes necessarias 
  para as futuras analises e comparacoes que podem ser usadas em sistemas 
  de terceiros, de forma a facilitar a forma como podem ser comparados
  """
  def __init__(self) -> None:
    self.raw_image_path = config.raw_image_dir
    self.processed_image_path = config.processed_image_dir

  @staticmethod
  def transform_image_in_array(self, id: int) -> None:
    """
    Metodo relacionado a receber a imagem presente dentro do sistema, de forma 
    a transformar ela em um array bidimensional de dados estruturados em pixels,
    de forma a facilitar e possibilitar o processamento por parte dos sistemas 
    e por parte dos outros metodos do sistema
    """
    if img is None and img_path is None:
      raise ValueError("It's necessary to pass the file or the file path")
    if img is None and img_path is not None:
      pass
    
    img = cv2.imread(img)
    print(img)
    return img

  @staticmethod
  def convert_image_to_grayscale(self, img: np.ndarray) -> None:
    pass
    

  @staticmethod 
  def normalize_image_hist(self) -> None:
    pass
