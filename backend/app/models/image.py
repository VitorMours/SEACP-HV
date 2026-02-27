from pathlib import Path
from sqlmodel import Field, SQLModel

class Image(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    was_processed: bool = Field(default=False)
    path: Path = Field(default=None)