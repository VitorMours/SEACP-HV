from schemas.image_schema import ImageCreationSchema
from models.image_model import ImageModel
import os 
from pathlib import Path
from fastapi import File
from config.paths import DIRECOTY_PATH


class ImageRepository:
  """
  ImageRepository funciona como um repositorio responsavel por modificar e 
  ditar o comportamento que temos ao usar o modelo de imagens presente dentro 
  do nosso banco de dados, de forma a nao termos que lidarmos com elementos tao
  diretos, e termos abstracoes que facilitam a forma como podemos desenvolver 
  os nossos sistemas.
  """
  
  DIRECTORY_PATH = DIRECOTY_PATH

  @staticmethod
  def save_image(name: str, file: ImageCreationSchema) -> None:
    pass
  
  @staticmethod
  def get_image_by_filename() -> None:
    pass
  
  @staticmethod
  def get_all_images() -> None:
    pass
  
  @staticmethod
  def delete_image() -> None:
    pass
  
  @staticmethod
  def soft_delete() -> None:
    pass
  
  @staticmethod
  def image_info() -> None:
    pass