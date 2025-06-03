from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# User schemas
class UserBase(BaseModel):
    username: str
    email: Optional[str] = None

class UserCreate(UserBase):
    pass  # You can include password here if needed

class User(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Category schemas
class CategoryBase(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryCreate(CategoryBase):
    pass

class Category(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Journal Entry schemas
class JournalEntryBase(BaseModel):
    title: str
    content: str
    user_id: int
    category_id: int

class JournalEntryCreate(JournalEntryBase):
    pass

class JournalEntryUpdate(BaseModel):
    title: str
    content: str

class JournalEntry(JournalEntryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
