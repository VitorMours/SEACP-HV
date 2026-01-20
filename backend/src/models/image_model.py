import os 
import uuid 
from backend.src.config.db import Base
from sqlalchemy import Column, String, Boolean, Integer, ForeignKey, DateTime

from datetime import datetime

class ImageModel(Base): 
  """
  Modelo representativo da entidade de imagem dentro do banco de dados,
  de forma que as informacoes serao armazenadas dentro do banco 
  de dados, mas que a imagem em si sera armazenada dentro de 
  de uma pasta ao lado do projeto.
  
  
  Estrategia de Persistencia de Dados:
  -----------------------------------
    A persistencia de dados como citado anteriormente, vai ter os 
    metadados da imagens armazenados dentro do banco de dados em si, 
    porem a imagem vai ser armazenada dentro de uma pasta, sendo salvo 
    dentro do banco de dados, a rota de acesso desse arquivo
    - Metadados: Banco de Dados (tb_images)
    - Imagem: Sistema de Arquivos (files/raw)
  
  Parametros:
  -----------
    name: str
    filepath: str
    mimetype: str
    processed: str
    created_at: timestamp
    updated_at: timestamp
    
  Retorno:
  ------- 
  
  """
  
  
  __tablename__ = "tb_images"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False) 
  filepath = Column(String(255), nullable=False)
  mimetype = Column(String(50))
  processed = Column(Boolean(False))
  created_at  = Column(DateTime, default=datetime.utcnow)
  updated_at  = Column(DateTime, default=datetime.utcnow)
  
  
  