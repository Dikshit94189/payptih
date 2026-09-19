from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.core.security import(
    create_access_token,
    verify_password
)

from app.repositories.user_repository import get_user_by_email
from app.schemas.auth import LoginRequest, LoginResponse

def login_user(
    db: Session,
    login_data: LoginRequest
) -> LoginRequest:
    
    # 1. Find user using email
    user = get_user_by_email(
        db,login_data.email
    )
    
    # 2. Check whether user exists
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or email Password"
        )
        
    # 3. Verify entered password against database hash
    password_is_valid = verify_password(
        login_data.password,
        user.password_hash
    )
    
    # 4. Check password
    if not password_is_valid:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED
            detail="Invalid email or password"
        )
    
    # 5. Create JWT access token

    access_token = create_access_token(
        user_id = user.id,
        email = user.email
    )
    
    # 6. Return login response
    
    return LoginResponse(
        access_token=access_token,
        token_type="bearer"
    )