"""Validation Schemes (Pydantic)"""
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str
    permission_level: Optional[str] = 'user'


class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    permission_level: str
    created_at: datetime

    class Config:
        orm_mode = True
