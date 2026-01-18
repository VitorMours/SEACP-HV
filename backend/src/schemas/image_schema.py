from pydantic import BaseModel 


class Image(BaseModel):
  name: str 
  mimetype: str 
  filepath: str

  class Config:
    from_attributes = True 
    
class ImageResponse(Image):
  """
  Image Response deve ter os seguintes atributos:
  
    name: str
    mimetype: str
    filepath: str
    success: bool
  """
  
  success: bool
  
  