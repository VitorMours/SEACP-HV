import glob
import os
from app.repository.image_repository import ImageRepository
from app.models.image import Image
import cv2
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns 
import pandas as pd
from pathlib import Path
from app.core.config import config
from app.schemas.image import ImageRead, ImageCreate
from fastapi import File
from sqlmodel import Session
import shutil
import base64
from app.core.logging import get_logger

logger = get_logger(__name__)    
  
      
      
class ImageProcessingService:
  """
  Servico focado no processamento de imagens e nas transfomacoes necessarias 
  para as futuras analises e comparacoes que podem ser usadas em sistemas 
  de terceiros, de forma a facilitar a forma como podem ser comparados
  """
  def __init__(self) -> None:
    self.raw_image_path = config.raw_image_dir
    self.processed_image_path = config.processed_image_dir
    self.gray_image_path = config.gray_image_dir

  def transform_image_in_array(self, img_base64: base64) -> None:
    """
    Metodo relacionado a receber a imagem presente dentro do sistema, de forma 
    a transformar ela em um array bidimensional de dados estruturados em pixels,
    de forma a facilitar e possibilitar o processamento por parte dos sistemas 
    e por parte dos outros metodos do sistema
    """
    image_bytes = base64.b64decode(img_base64)
    np_array = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Não foi possível decodificar a imagem")
    return img

  def convert_image_to_grayscale(self, img_base64: ImageRead) -> None:
    image_bytes = base64.b64decode(img_base64.image)
    filename = img_base64.image_name
    output_path = os.path.join(self.gray_image_path, f"{filename}_gray.png")
    np_array = np.frombuffer(image_bytes, dtype=np.uint8)
    img = cv2.imdecode(np_array, cv2.IMREAD_GRAYSCALE)
    success = cv2.imwrite(output_path, img)
    
    if success is None:
        raise ValueError("Não foi possível decodificar a imagem")
    return img

  def _normalize_image_hist(self, np_img: np.ndarray) -> None:
    img_equalized = cv2.equalizeHist(np_img)
    return img_equalized
    
  def process_image(self, image: ImageRead) -> None:
    filename = image.image_name
    gray_image = self.convert_image_to_grayscale(image)
    normalized_image = self._normalize_image_hist(gray_image)
    output_path = os.path.join(self.processed_image_path, f"{filename}_processed.png")
    cv2.imwrite(output_path, normalized_image)
    return normalized_image
   


  def generate_image_histogram(self, image: ImageRead) -> None:
      """
        Funcao de processamento de image, focada em receber uma imagem,
        e gerar um histograma da mesma de forma que 
      """
      
      pass




















  def _save_img(self, image, path: Path) -> None:
    pass
    
    
    
    
