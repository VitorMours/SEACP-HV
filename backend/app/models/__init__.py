from sqlmodel import create_engine, SQLModel, Session
from .image import Image
from .user import User

engine = create_engine("sqlite:///db.sqlite3")

def create_tables():
  SQLModel.metadata.create_all(engine)
  
def get_session():
  with Session(engine) as session:
    yield session