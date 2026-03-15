from pydantic import BaseModel

class ImageRead(BaseModel):
  id: int | None = None 
  image_name: str
  image: str | None = None
  filetype: str
  path: str

  @property
  def url(self) -> str:
    return f"http://localhost:8000/media/raw/{self.image_name}"


class ImageCreate(BaseModel):
  id: int | None = None 
  image_name: str
  filetype: str

class ImageUpdate(BaseModel):
  pass

class ImageDelete(BaseModel):
  pass
