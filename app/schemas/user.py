from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):
    """Base schema for user data."""
    email: EmailStr = Field(..., example="user@example.com")


class UserCreate(UserBase):
    """Schema used during user registration."""
    password: str = Field(..., min_length=8, example="strongPassword123")


class UserOut(UserBase):
    """Schema returned in responses (e.g., after registration or login)."""
    id: int = Field(..., example=1)
    is_active: bool = Field(default=True, example=True)

    class Config:
        orm_mode = True