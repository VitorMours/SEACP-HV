from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

local_path = Path(__file__).parent.parent.absolute()


class Config(BaseSettings):
    app_name: str = "SEACP"
    images_dir: Path = local_path / "media"
    raw_image_dir: Path = local_path / "media" / "raw"
    processed_image_dir: Path = local_path / "media" / "processed"
    gray_image_dir: Path = local_path / "media" / "gray"


config = Config()