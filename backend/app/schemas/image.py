from pydantic import BaseModel

class ImageRead(BaseModel):
  image_name: str
  image: str
  filetype: str
  path: str

class ImageCreate(BaseModel):
  image_name: str
  filetype: str

class ImageUpdate(BaseModel):
  pass

class ImageDelete(BaseModel):
  pass
