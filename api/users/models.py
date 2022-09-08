from sqlalchemy import Column, Integer, String, Boolean
from configuration.db import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, unique=True, index=True)
    login = Column(String, unique=True)
    name = Column(String)
    password = Column(String)

    is_admin = Column(Boolean, default=False)
    is_owner = Column(Boolean, default=False)
