import pytest 
import inspect 
import importlib 




class TestImageService:
    def test_if_image_service_module_exists(self) -> None:
        try:
            from services import image
            assert image is not None 
        except ImportError:
            raise ImportError("Was not possible to import the service module")

    def test_if_image_service_module_have_image_service_class(self) -> None:
        try:
          from services.image import ImageService 
          assert ImageService is not None 
          assert inspect.isclass(ImageService)
        except ImportError:
          raise ImportError("Was not possible to import the ImageService class")


    def test_if_image_service_module_have_image_service_processing_class(self) -> None:
        try:
            from services.image import ImageProcessingService
            assert ImageProcessingService is not None 
            assert inspect.isclass(ImageProcessingService)
        except ImportError:
            raise ImportError("Was not possible to import the ImageProcessingService class")
