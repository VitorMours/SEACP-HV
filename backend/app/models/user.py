from pydantic import EmailStr
from sqlmodel import SQLModel, Field

class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    first_name: str = Field(nullable=False)
    last_name: str
    email: EmailStr = Field(nullable=False)
    password: str = Field(nullable=False)
