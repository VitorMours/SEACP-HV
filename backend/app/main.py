from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import config
from app.api import api_router
from app.utils.files import create_media_file_structure
from app.models import create_tables
from app.core.logging import get_logger


create_media_file_structure(config.images_dir)
create_tables()
get_logger(__name__)

app = FastAPI(title = config.app_name)

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],     
)

app.include_router(api_router)
