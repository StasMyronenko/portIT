from pydantic import BaseModel


class ProjectBase(BaseModel):
    id: int
    title: str
    description: str
    url: str
    photo_url: str

    class Config:
        orm_mode = True
