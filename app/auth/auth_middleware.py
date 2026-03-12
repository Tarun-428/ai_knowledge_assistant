from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer
from jose import jwt

from app.auth.auth_handler import SECRET_KEY, ALGORITHM

security = HTTPBearer()


def get_current_user(token=Depends(security)):

    try:
        payload = jwt.decode(
            token.credentials,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        return payload

    except Exception:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication token"
        )