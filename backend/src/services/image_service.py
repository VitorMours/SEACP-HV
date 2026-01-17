from fastapi import File
import shutil
from pathlib import Path
import pandas as pd 
import numpy as np 

class ImageService:
    
    @staticmethod
    def ingest_image_in_server(file_directory_path: str, file: File) -> None:
        try:
            file_location = file_directory_path / file.filename
            with open(file_location, "wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            return file_location
        except Exception:
            return False
            
    @staticmethod 
    def process_image() -> None:
        pass