from datetime import datetime, timedelta
from jose import jwt
from app.core.secrets import secrets_provider
from jose import jwt, JWTError
from fastapi import HTTPException, status
from app.core.secrets import secrets_provider

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 15

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    secret = secrets_provider.get_secret("JWT_SECRET")
    return jwt.encode(to_encode, secret, algorithm=ALGORITHM)

def decode_token(token: str):
    secret = secrets_provider.get_secret("JWT_SECRET")
    try:
        payload = jwt.decode(token, secret, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )