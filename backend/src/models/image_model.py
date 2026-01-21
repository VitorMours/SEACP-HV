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
    name : str
      Nome do arquivo que o usuário visualiza de forma a facilitar a manipulação dele
    
    filepath : str
      Nome do arquivo em si, representa o caminho que termos que fazer para 
      acessar essas imagens dentro do nosso sistemas
    
    mimetype : str
      O tipo de arquivo que estamos usando, de forma a facilitar o entendimento 
      de com quais tipos de arquivos estamos trabalhando
    
    processed : boolean
      Variavel booleana responsavel por dizer se essa determinada imagem ja 
      foi processada, ou ainda precisa passar pelo processamento de imagens 
      do sistema
    
    created_at: timestamp
      Variavel nao modificavel que determina em que momento algum determinado 
      registro foi criado dentro do sistema do banco de dados 
      
    updated_at: timestamp
      Variavel nao modificavel que determina em que momento algum determinado 
      registro foi modificado dentro do sistema do banco de dados
      
  Retorno:
  ------- 
    Temos como retorno, a entidade dentro do bancos que representa a imagem 
    dentro do sistema fisico, e o relacionmento dela com o nosso usuario
  """
  
  __tablename__ = "tb_images"
  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, nullable=False) 
  filepath = Column(String, nullable=False, unique=True)
  mimetype = Column(String(50))
  processed = Column(Boolean(False))
  created_at  = Column(DateTime, default=datetime.utcnow)
  updated_at  = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  
  
  def __str__(self) -> None:
    return f"ImageModel(id={self.id}, name={self.name}, mimetype={self.mimetype}, processed={self.processed})"
  
  