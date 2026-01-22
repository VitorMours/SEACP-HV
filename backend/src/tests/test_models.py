from sqlalchemy.orm import Session 
import importlib 
from sqlalchemy import inspect


class TestImageModel:
  def test_if_can_import_image_model_class(self) -> None:
    try:
      from models.image_model import ImageModel
    except ImportError:
      raise ImportError("Was not possible to import ImageModel")
    
  def test_if_model_have_correct_fields(self) -> None:
    try:
      from models.image_model import ImageModel
      inspector = inspect(ImageModel)
      expected_columns = ['id', 'name', 'filepath', 'mimetype', '_processed', 'created_at', 'updated_at']
      assert expected_columns == [col.key for col in inspector.columns]
    except ImportError:
      raise ImportError("Was not possible to import ImageModel")
    
    
  def test_if_can_create_image_model(self) -> None:
    try:
      from models.image_model import ImageModel 
      image = ImageModel(
        name = "Creating image",
        filepath = "d://image/new.jpeg",
        mimetype = "image/jpeg",
        processed = True
      )
      assert isinstance(image, ImageModel)
      assert image.name == "Creating image"
      assert image.processed == True
      assert image.mimetype == "image/jpeg"
      
    except Exception as e:
      raise e
    
  def test_if_can_toggle_processed_status_in_image(self) -> None:
    try:
      from models.image_model import ImageModel 
      image = ImageModel(
        name="new image",
        filepath="d://image.png", 
        mimetype="image/png",
        processed=True,
      )
      assert image.processed == True 
      image.processed = False
      assert image.processed == False
    except Exception as e:
      raise e
    
  def test_if_processed_getter_and_setter_manipulate_value_passed(self) -> None: 
    try:
      from models.image_model import ImageModel 
      image = ImageModel( 
        name="new image",
        filepath="d://image.png", 
        mimetype="image/png",
        processed=True
      )
      image.processed = 0
      assert image.processed == False
    except Exception as e:
      raise e 
    
  def test_if_image_model_representation_exists(self) -> None:
    try:
      from models.image_model import ImageModel 
      image = ImageModel( 
        name="new image",
        filepath="d://image.png", 
        mimetype="image/png",
        processed=True
      )
      image.processed = 0
      assert str(image) == f"ImageModel(id={image.id}, name={image.name}, mimetype={image.mimetype}, processed={image.processed})"
    except Exception as e:
      raise e 
    