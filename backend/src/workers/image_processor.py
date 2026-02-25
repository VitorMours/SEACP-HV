import os 
from config.paths import DIRECOTY_PATH
from pathlib import Path
from celery import Celery 
from src.services.image_processing_service import ImageProcessingService
import cv2 

cl = Celery('image_processor', 
  broker="redis://redis:6379/0", 
  backend="redis://redis:6379/0"
)


@cl.task(name="process_image_in_grayscale")
def process_image_in_grayscale(filename: str):
  raw_path = DIRECOTY_PATH / "raw" / filename
  gray_path = DIRECOTY_PATH / "processed" / "gray"
  gray_path.parent.mkdir(exist_ok=True, parents=True)
   
  img_np = cv2.imread(str(raw_path))
  if img_np is None:
   return f"Erro: Arquivo {filename} não encontrado."

  gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
  cv2.imwrite(str(gray_path), gray_img)
  return f"Sucesso: {filename} processado."   