import datetime

from fastapi import Request, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from starlette import status

from configuration.settings import SECRET_KEY, ALGORITHM
from users.schemas import PayloadUser


def get_db(request: Request):
    return request.state.db


def get_site_db(request: Request):
    return request.state.site_data_db

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_current_user(token: str = Depends(oauth2_scheme)) -> PayloadUser:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # authorization = authorization.split(' ')[1]
        if not token:
            raise credentials_exception
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if datetime.datetime.utcfromtimestamp(payload['exp']) < datetime.datetime.utcnow():
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    except Exception as e:
        print(e)
        raise credentials_exception
    return PayloadUser(**payload)


