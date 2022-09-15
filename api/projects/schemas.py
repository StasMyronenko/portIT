from pydantic import BaseModel
import json
from sqlalchemy import TypeDecorator, Unicode


class ProjectBase(BaseModel):
    id: int
    title: str
    description: str
    url: str
    photo_url: str

    class Config:
        orm_mode = True


class Json(TypeDecorator):
    """
        As I understand here we change type of data to str and when we use it function process_result_value changes it back
    """
    impl = Unicode

    def process_bind_param(self, value, engine):
        return json.dumps(value)

    def process_result_value(self, value, engine):
        if value is None:
            return None

        return json.loads(value)
