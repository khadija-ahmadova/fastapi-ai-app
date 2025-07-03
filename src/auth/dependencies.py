from typing import Optional
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer


SECRET_KEY = "very-secret-key"
ALGORITHM = "HS256"

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token", auto_error=False)

async def get_user_identifier(token: Optional[str] = Depends(oauth_scheme)):
    if token is None:
        return "global_unauthenticateduser"
    
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    username: str = payload.get("sub")
    return username

