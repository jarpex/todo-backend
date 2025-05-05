from datetime import datetime, timedelta, timezone
from typing import Optional, Dict, Any

from jose import jwt

from app.core.config import settings


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """Generate a JWT access token with a UTC-aware expiration timestamp."""
    payload = data.copy()
    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
    payload["exp"] = expire

    return jwt.encode(payload, settings.JWT_SECRET_KEY, algorithm=settings.ALGORITHM)