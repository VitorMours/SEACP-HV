import uvicorn
from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware 
from utils.image_utils import build_file_structure
import routes
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

# Funcoes que precisam ser usadas
build_file_structure()

if __name__ == "__main__":
    uvicorn.run("src.main:app", host="0.0.0.0", port=8000, reload=True)