from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import config
from app.api.v1.image import router as image_router
from app.utils.files import create_media_file_structure
from app.models import create_tables

create_media_file_structure(config.images_dir)
create_tables()



app = FastAPI(title = config.app_name)
app.include_router(image_router)
