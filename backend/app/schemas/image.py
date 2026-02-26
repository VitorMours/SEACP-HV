from pydantic import BaseModel

class ImageRead(BaseModel):
  pass

class ImageCreate(BaseModel):
  image_name: str
  filetype: str

class ImageUpdate(BaseModel):
  pass

class ImageDelete(BaseModel):
  pass
