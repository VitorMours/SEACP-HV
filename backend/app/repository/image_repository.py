from app.models.image import Image 
from app.models import get_session
from sqlmodel import Session

class ImageRepository:
  def __init__(self, session: Session) -> None:
    self.session = session
  
  def save_image(self, image: Image) -> None:
    self.session.add(image)
    self.session.commit()
    self.session.refresh(image)
    
  def fetch_image_by_id(self, id: int) -> Image | None:
    return self.session.get(Image, id)
  
  def fetch_image(self) -> None:
    pass
    