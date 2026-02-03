from pathlib import Path
import pandas as pd 
import numpy as np 
import cv2
import io 
from config.paths import DIRECOTY_PATH

class ImageProcessingService:
  @staticmethod
  def process_image(img) -> np.ndarray | None:
    directory_path = DIRECOTY_PATH
    filepath = directory_path / "raw" / img
    
    if not filepath.exists():
      print(f"Error: File not found at {filepath}")
      return None

    img_np: np.ndarray = cv2.imread(str(filepath))
    return img_np
  
  @staticmethod
  def generate_gray_scale_image_version(img_np: np.ndarray) -> np.ndarray:
    gray_img = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)
    success, buffer = cv2.imencode(".jpg", gray_img)
    
    if not success:
        raise ValueError("Não foi possível codificar a imagem")
    
    return buffer.to_bytes()
  