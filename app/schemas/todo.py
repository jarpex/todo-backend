from pydantic import BaseModel, Field
from typing import Optional


class TodoBase(BaseModel):
    """Shared fields for a to-do item."""
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Eggs, Bread")
    done: bool = Field(False, example=False)


class TodoCreate(TodoBase):
    """Fields required to create a new to-do item."""
    pass


class TodoUpdate(BaseModel):
    """Fields that can be updated in a to-do item."""
    title: Optional[str] = Field(None, example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, Eggs, Bread")
    done: Optional[bool] = Field(None, example=True)


class TodoOut(TodoBase):
    """Response model for returning a to-do item."""
    id: int
    owner_id: int

    class Config:
        orm_mode = True