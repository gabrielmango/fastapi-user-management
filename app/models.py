"""Modelos do banco (SQLAlchemy)"""
from datetime import datetime

from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.sql.sqltypes import DateTime

from app.database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    permission_level = Column(
        Enum('admin', 'user'), name='permission_level', default='user'
    )
    created_at = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'User(name="{self.name}", email="{self.email}")'
