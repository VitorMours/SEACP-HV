from app.repository.image_repository import ImageRepository
from .celery import celery_app 
from app.services.image_processing import ImageProcessingService
from sqlmodel import Session
from app.models import engine
from app.services.image import ImageService

@celery_app.task(name="app.workers.image.process_image_to_histogram_analysis") 
def process_image_to_histogram_analysis(image_id: int):
  with Session(engine) as session:
    repository = ImageRepository(session)
    image_service = ImageService(repository)
    processing_service = ImageProcessingService()

    image = image_service.return_image_by_id(image_id)
    array = processing_service.process_image(image)

