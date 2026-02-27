from sqlmodel import create_engine, SQLModel
from .image import Image
from .user import User

engine = create_engine("sqlite:///db.sqlite3")

SQLModel.metadata.create_all(engine)