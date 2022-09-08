from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: str | None = None
    name: str | None = None
    login: str | None = None
    is_admin: bool | None = None
    is_owner: bool | None = None
