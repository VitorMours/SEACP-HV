import os 
import uuid 
from backend.src.config.db import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime

from datetime import datetime


class ImageModel(Base): 
  """
  Modelo usado para armazenar referencias e outros elementos das imagens 
  dentro de um determinado banco de dados  
  """
  __tablename__ = "tb_images"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False) 
  filepath = Column(String(255), nullable=False)
  mimetype = Column(String(50))
  created_at  = Column(DateTime, default=datetime.utcnow)
  updated_at  = Column(DateTime, default=datetime.utcnow)
  
  
  