from pydantic import BaseModel
from typing import Optional

# Basic schema for todo item
class TodoBase(BaseModel):
    title: str
    description: Optional[str] = None
    done: bool = False

# Task creation
class TodoCreate(TodoBase):
    pass

# Task update
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    done: Optional[bool] = None

# Response
class TodoOut(TodoBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True