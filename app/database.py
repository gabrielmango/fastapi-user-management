"""SQLite Database Configuration"""

from dotenv import dotenv_values
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

config = dotenv_values('.env')

DATABASE_NAME = config['DATABASE_URL']

engine = create_engine(
    DATABASE_NAME, connect_args={'check_same_thread': False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """Return the database"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
