from pwdlib import PasswordHash
import jwt
from pwdlib import PasswordHash

from datetime import datetime, timedelta, timezone

from app.config.config import(
    JWT_ALGORITHM,
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES,
    JWT_SECRET_KEY
)

password_hash = PasswordHash.recommended()

def hash_password(password: str) -> str:
    return password_hash.hash(password)

def verify_password(
    plain_password: str,
    hashed_password: str,
)-> bool:
    return password_hash.verify(
        plain_password,
        hashed_password
    )
    
def create_access_token(
    user_id : int,
    email: str
) -> str:
    expire = datetime.now(timezone.utc) + timedelta(
        minutes=JWT_ACCESS_TOKEN_EXPIRE_MINUTES
    )    
    
    payload = {
        "sub" : str(user_id),
        "email" : email,
        "exp" : expire
    }
    
    token = jwt.encode(
        payload,
        JWT_SECRET_KEY,
        algorithm = JWT_ALGORITHM
    )
    
    return token
        