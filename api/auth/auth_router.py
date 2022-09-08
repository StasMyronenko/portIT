from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status

from auth.auth_service import authenticate_user, create_access_token, create_user
from auth.models import Token
from auth.schemas import RegisterData
from configuration.utils import get_db

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@router.post("/register")
async def register_user(response: Response, db: Session = Depends(get_db), data: RegisterData = Depends()):

    try:
        return await create_user(db, data)
    except:  # TODO. Make normal exceptions
        response.status_code = 401
        return {"message": "Can't register"}


@router.post("/login", response_model=Token)
async def login_user(response: Response, db: Session = Depends(get_db), data: OAuth2PasswordRequestForm = Depends()):
    print(data)
    user = authenticate_user(db, data.username, data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    data = {"id": user.id, "login": user.login, "is_admin": user.is_admin, "is_owner": user.is_owner}
    access_token = create_access_token(data)
    # response.set_cookie(key="jwt_token", value=access_token)
    return {"access_token": access_token, "token_type": "bearer"}
