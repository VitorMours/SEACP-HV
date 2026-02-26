from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from app.core import config

app = FastAPI(title = config.app_name)


