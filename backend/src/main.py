from config.logging import setup_logging
from config.db import Base, engine
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from utils.image_utils import build_file_structure
import routes
import logging

# Configura o logging ANTES de criar o app
logs_dir = setup_logging()
logger = logging.getLogger(__name__)

logger.info("=" * 50)
logger.info("Iniciando aplicação FastAPI")
logger.info(f"Logs serão salvos em: {logs_dir}")
logger.info("=" * 50)

# Database configuration
# Creating the app
Base.metadata.create_all(bind=engine)
build_file_structure()





app = FastAPI(title="SEACPHV API") 




origins = [
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost",
]

# App midlewares 
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def global_index():
    return {"Hello":"World"}


app.include_router(routes.router)
