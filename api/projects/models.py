from sqlalchemy import Column, Integer, String, Text
from configuration.db import Base


class Project(Base):
    __tablename__ = "project"

    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    url = Column(String)
    photo_url = Column(String)
