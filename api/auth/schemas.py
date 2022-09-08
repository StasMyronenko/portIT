from typing import Optional

from fastapi import Body, Form
from fastapi.security import OAuth2PasswordRequestForm


class OAuth2PasswordRequestBody(OAuth2PasswordRequestForm):
    """
    For use OAuth with Content-Type: application/json, not form data
    """
    def __init__(
        self,
        grant_type: str = Body(regex="password", default="password"),
        username: str = Form(),
        password: str = Form(),
        scope: str = Body(default=""),
        client_id: Optional[str] = Body(default=None),
        client_secret: Optional[str] = Body(default=None),
    ):
        super().__init__(
            grant_type=grant_type,
            username=username,
            password=password,
            scope=scope,
            client_id=client_id,
            client_secret=client_secret,
        )


class RegisterData:
    def __init__(
            self,
            login: str = Body(),
            name: str = Body(),
            password: str = Body(),
            repeat_password: str = Body()

    ):
        self.login = login
        self.name = name
        self.password = password
        self.repeat_password = repeat_password
