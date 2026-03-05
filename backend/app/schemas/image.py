from pydantic import BaseModel

class ImageRead(BaseModel):
  id: int | None = None 
  image_name: str
  image: str
  filetype: str
  path: str

class ImageCreate(BaseModel):
  id: int | None = None 
  image_name: str
  filetype: str

class ImageUpdate(BaseModel):
  pass

class ImageDelete(BaseModel):
  pass
