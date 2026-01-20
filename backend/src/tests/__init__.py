import logging
import pytest 
import sqlalchemy 
from sqlalchemy.orm import sessionmaker, Session, Engine
from sqlalchemy.exc import IntegrityError
from datetime import datetime 
import uuid

from config.db import Base

TEST_DATABASE_URI = "sqlite:///:memory:"
@pytest.fixture(scope="function")
def create_engine() -> Engine:
  engine = create_engine(TEST_DATABASE_URI,         
    connect_args={"check_same_thread": False}
  )
  Base.metadata.create_all(bind=engine)
  yield engine 
  Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def session(engine) -> Session:
  SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  session = SessionLocal()
  yield session 
  session.close()
