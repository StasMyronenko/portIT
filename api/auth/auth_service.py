from datetime import timedelta, datetime

from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from auth.schemas import RegisterData
from configuration.settings import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from users.models import User
from users.schemas import GetUser

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


async def create_user(db: Session, data: RegisterData):
    users = db.query(User).where(User.login == data.login).all()
    if data.password == data.repeat_password:
        if len(users) == 0:
            hashed_password = hash_password(data.password)
            user = User(login=data.login, name=data.name, password=hashed_password)
            db.add(user)
            db.commit()
            return {"message": 'OK'}
        raise {"message": "This email already exists"}  # TODO. make it normal error
    raise {"message": "passwords aren't the same"}  # TODO. make it normal error


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(password, hashed_password):
    return pwd_context.verify(password, hashed_password)


def authenticate_user(db: Session, login, password) -> GetUser | bool:
    user = db.query(User).where(User.login == login).first()
    if user and verify_password(password, user.password):
        return user
    else:
        return False


def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    payload = data.copy()
    payload.update({"exp": datetime.utcnow() + expires_delta})
    encoded_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
