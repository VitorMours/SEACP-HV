import sys
import os
import pytest
import importlib 
import inspect
# Ensure both project root and backend/src are on sys.path so both
# absolute imports (backend.src...) and direct imports (repositories...) work
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)
sys.path.insert(0, src_path)

class TestImageRepository:
  def test_if_can_import_the_file(self) -> None:
      try:
          from repositories import image_repository
      except Exception as e:
          raise ImportError("Nao foi possivel importar o repository de imagens") from e
  
  def test_if_can_import_the_class(self) -> None: 
    try:
      from repositories.image_repository import ImageRepository
    except Exception as e:
          raise ImportError("Nao foi possivel importar o repository de imagens") from e
      
  def test_instanciate_the_class(self) -> None:
    try:
      module = importlib.import_module("repositories.image_repository")
      class_ = module.ImageRepository
    except Exception as e:
      raise e
    
  def test_if_image_repository_have_same_image_method(self) -> None:
    module = importlib.import_module("repositories.image_repository")
    class_ = module.ImageRepository 
    assert hasattr(class_, "save_image")
    
  def test_if_image_repository_have_get_all_images_method(self) -> None:
    module = importlib.import_module("repositories.image_repository")
    class_ = module.ImageRepository
    assert hasattr(class_, "get_all_images")
    
  def test_if_image_repository_have_get_image_by_filename_method(self) -> None:
    module = importlib.import_module("repositories.image_repository")
    class_ = module.ImageRepository
    assert hasattr(class_, "get_image_by_filename")
    
  def test_if_image_repository_have_delete_method(self) -> None:
    module = importlib.import_module("repositories.image_repository")
    class_ = module.ImageRepository
    assert hasattr(class_, "delete_image")
    
  def test_if_image_repository_have_soft_delete_method(self) -> None:
    module = importlib.import_module("repositories.image_repository")
    class_ = module.ImageRepository
    assert hasattr(class_, "soft_delete")