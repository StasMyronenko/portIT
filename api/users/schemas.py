from pydantic import BaseModel


class UserBase(BaseModel):
    login: str

    class Config:
        orm_mode = True


class UserRegister(UserBase):
    password: str
    replace_password: str
    name: str


class UserLogin(UserBase):
    password: str


class GetUser(UserBase):
    id: int
    name: str
    is_admin: bool
    is_owner: bool


class PayloadUser(UserBase):
    id: int
    is_admin: bool
    is_owner: bool
