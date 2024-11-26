"""Routes for user management"""
from fastapi import APIRouter, Depends
from passlib.hash import bcrypt
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db
from app.exceptions import HttpError

router = APIRouter(prefix='/users', tags=['Users'])


@router.post('/', response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """Creates a new user."""

    existing_user = (
        db.query(models.User).filter(models.User.email == user.email).first()
    )

    if existing_user:
        HttpError.user_already_exists()

    hashed_password = bcrypt.hash(user.password)
    new_user = models.User(
        name=user.name,
        email=user.email,
        password_hash=hashed_password,
        permission_level=user.permission_level,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@router.get('/', response_model=list[schemas.UserResponse])
def list_all_users(db: Session = Depends(get_db)):
    """Returns a list of all users."""
    users = db.query(models.User).all()

    if users:
        return users
    return []


@router.get('/{user_id}', response_model=schemas.UserResponse)
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    """Returns a user by their ID."""
    user = db.query(models.User).filter(models.User.id == user_id).first()

    if user:
        return user
    raise HttpError.not_found(f'User id {user_id}')
