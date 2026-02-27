from pydantic import BaseModel

class ImageRead(BaseModel):
  image_name: str
  image: bytes
  filetype: str
  path: str

class ImageCreate(BaseModel):
  image_name: str
  filetype: str

class ImageUpdate(BaseModel):
  pass

class ImageDelete(BaseModel):
  pass
