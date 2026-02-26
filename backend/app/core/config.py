from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config(BaseSettings):
  app_name: str = "SEACP"
  file_dir: str = ""



config = Config