from pydantic import BaseModel 

class UserRead(BaseModel):
    id: int
    first_name: str
    last_name: str 
    email: str 

class UserCreate(BaseModel):
    first_name: str 
    last_name: str 
    email: str 
    password: str 

class UserDelete(BaseModel):
    pass 

class UserUpdate(BaseModel):
    pass
