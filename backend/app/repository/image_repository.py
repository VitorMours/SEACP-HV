from app.models.image import Image 
from app.models import get_session
from sqlmodel import Session
from app.core.logging import get_logger

logger = get_logger(__name__)

class ImageRepository:
  def __init__(self, session: Session) -> None:
    self.session = session
  
  def save_image(self, image: Image) -> None:
    logger.info("Saving image in the folder")
    self.session.add(image)
    self.session.commit()
    self.session.refresh(image)
    
  def fetch_image_by_id(self, id: int) -> Image | None:
    logger.info("Fetching image by id")
    return self.session.get(Image, id)
  
  def fetch_image(self) -> None:
    pass
    