from fastapi.security import OAuth2PasswordBearer
from sqlalchemy_media import StoreManager
from starlette.requests import Request

from sqladmin import ModelView
from wtforms import StringField, Form, TextAreaField, URLField, FileField

from configuration.db import SessionLocal
from configuration.utils import get_current_user
from projects.models import Project, ProjectImage
from users.models import User

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# I need as cookie data as header because i use header in my app and redirect works correct when i use cookie data


class ForAdmin(ModelView):
    def is_accessible(self, request: Request) -> bool:
        header_token = request.cookies.get('jwt_token')
        lst = header_token.split() if header_token else None
        if (not lst) and request.headers['authorization']:
            lst = request.headers['authorization'].split()
        if lst and len(lst) > 1:
            token = lst[1]
        elif lst:
            token = lst[0]
        else:
            return False

        current_user = get_current_user(token)
        if current_user.is_admin:
            return True
        return False

    def is_visible(self, request: Request) -> bool:
        return self.is_accessible(request)


class ForOwner(ModelView):
    def is_accessible(self, request: Request) -> bool:
        header_token = request.cookies.get('jwt_token')
        lst = header_token.split() if header_token else None
        if (not lst) and request.headers['authorization']:
            lst = request.headers['authorization'].split()
        if lst and len(lst) > 1:
            token = lst[1]
        elif lst:
            token = lst[0]
        else:
            return False

        current_user = get_current_user(token)
        if current_user.is_owner:
            return True
        return False

    def is_visible(self, request: Request) -> bool:
        return self.is_accessible(request)


class ImageField(StringField):
    def process_formdata(self, list_value):
        if len(list_value) > 0:
            with StoreManager(SessionLocal):
                self.data = ProjectImage.create_from(list_value[0])


class ProjectForm(Form):
    title = StringField('title')
    description = TextAreaField('description')
    url = URLField('url')
    photo_url = ImageField('Photo Url')


class ProjectView(ForAdmin, model=Project):
    column_list = [Project.id, Project.title]
    form = ProjectForm


class UserView(ForOwner, model=User):
    column_list = [User.id, User.name, User.login]
