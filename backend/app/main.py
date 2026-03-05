from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import config
from app.api import api_router
from app.utils.files import create_media_file_structure
from app.models import create_tables

create_media_file_structure(config.images_dir)
create_tables()



app = FastAPI(title = config.app_name)
<<<<<<< HEAD

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  
    allow_methods=["*"],     
    allow_headers=["*"],     
)

app.include_router(api_router)
=======
app.include_router(image_router)
>>>>>>> a9f71f83fa96be52eb733160fd28d8b073155a4e
