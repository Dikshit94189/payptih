from sqlalchemy.orm import Session
from app.repositories.user_repository import get_all_users

def get_users(db: Session):
    return get_all_users(db)