from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.auth import LoginRequest, LoginResponse
from app.service.auth_service import login_user

router = APIRouter(
    prefix="/auth"
    tags=["Authentication"]
)