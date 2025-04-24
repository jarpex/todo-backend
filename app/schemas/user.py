from pydantic import BaseModel, EmailStr

# Basic schema for user
class UserBase(BaseModel):
    email: EmailStr

# On registration (with password)
class UserCreate(UserBase):
    password: str

# Response without password
class UserOut(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True