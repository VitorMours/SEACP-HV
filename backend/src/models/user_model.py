from sqlalchemy import String, Integer, DateTime, Boolean, Column  
from datetime import datetime 
import os 
from backend.src.config.db import Base



class UserModel(Base):
  """
  Modelo que representa os usuarios dentro da plataforma, de forma a facilitar
  o relacionamento entre as imagens, e seus proprietarios futuramente.
  
  Parametros:
  -----------
    id
    name
    email
    password
    is_active
    created_at
    updated_at
  
  Retorno:
  --------
  """
  
  __tablename__ = "tb_users"

  id = Column(Integer, primary_key = True, index = True)
  name = Column(String)
  email = Column(String, nullable=False, unique=True)
  password = Column(String, nullable=False)
  is_active = Column(Boolean, default=True)
  created_at = Column(DateTime, default=datetime.utcnow)
  updated_at = Column(DateTime, default=datetime.utcnow)