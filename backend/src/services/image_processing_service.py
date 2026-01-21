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
  def generate_graphical_image_representation() -> None:
    pass
  