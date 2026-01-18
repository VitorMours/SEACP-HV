from sqlalchemy.ext.declarative import declarative_base 
from sqlalchemy.orm import sessionmaker 
from sqlalchemy import create_engine

url = f"sqlite:///teste.sqlite3"

engine = create_engine(url, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
