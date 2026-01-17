from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

from app.config import settings

# -----------------------------
# OAuth2 Scheme
# -----------------------------
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/token")

# -----------------------------
# JWT Config
# -----------------------------
ALGORITHM = "HS256"


# -----------------------------
# Token Utilities
# -----------------------------
def create_access_token(
    data: dict, expires_delta: Optional[timedelta] = None
) -> str:
    """
    Creates a signed JWT access token.
    """
    to_encode = data.copy()

    expire = datetime.utcnow() + (
        expires_delta
        if expires_delta
        else timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=ALGORITHM
    )
    return encoded_jwt


def verify_token(token: str) -> dict:
    """
    Verifies JWT token and returns payload.
    """
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[ALGORITHM]
        )
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )


# -----------------------------
# Dependency
# -----------------------------
def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """
    FastAPI dependency to protect routes.
    """
    return verify_token(token)
