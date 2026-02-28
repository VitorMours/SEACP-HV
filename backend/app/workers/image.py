from .celery import celery_app 
from app.services.image_processing import ImageProcessingService


@celery_app.task(name="app.workers.image.convert_to_grayscale") 
def convert_image_to_gray_scale():
  pass
  
