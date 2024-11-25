"""Main file to initialize the app"""
from fastapi import FastAPI

from app.database import Base, engine
from app.routers import users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(users.router)


@app.get('/')
def root():
    """Default endpoint for the API"""
    return {'message': 'Welcome to the FastAPI User API'}
