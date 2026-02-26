from pydantic import BaseModel 
import importlib 
import pytest 
import inspect 


class TestImageSchemas:
  def test_if_can_import_image_module(self) -> None:
    try:
      from app.schemas import image
      assert image is not None 
    except ImportError:
      raise ImportError("Was not possible to import the image schemas")
    
  def test_if_image_schemas_module_have_classes(self) -> None:
    try:
      from app.schemas.image import ImageCreate, ImageRead, ImageUpdate, ImageDelete
      assert ImageCreate is not None 
      assert ImageRead is not None 
      assert ImageUpdate is not None 
      assert ImageDelete is not None 
      assert inspect.isclass(ImageCreate)
      assert inspect.isclass(ImageUpdate)
      assert inspect.isclass(ImageRead)
      assert inspect.isclass(ImageDelete)
    except ImportError:
      raise ImportError("Was not possible ot import all the schemas from the module")
    
  def test_if_image_schemas_have_correct_superclass(self) -> None:
    module = importlib.import_module("app.schemas.image")
    create_class_ = module.ImageCreate
    assert issubclass(create_class_, BaseModel)
    read_class_ = module.ImageRead
    assert issubclass(read_class_, BaseModel)
    update_class_ = module.ImageUpdate
    assert issubclass(update_class_, BaseModel)
    delete_class_ = module.ImageDelete
    assert issubclass(delete_class_, BaseModel)
  
  def test_if_image_create_schema_have_correct_fields(self) -> None:
    module = importlib.import_module("app.schemas.image")
    class_ = module.ImageCreate
    fields = class_.model_fields
    assert "image_name" in fields
    assert "filetype" in fields

  def test_if_image_read_schema_have_correct_fields(self) -> None:
    module = importlib.import_module("app.schemas.image")
    class_ = module.ImageRead
    fields = class_.model_fields
    assert "image_name" in fields
    assert "filetype" in fields
    assert "path" in fields
