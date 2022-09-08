from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import pymongo
from dotenv import load_dotenv
load_dotenv()
# ##  SQL  ## #
SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, echo=True, future=True, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# ##  NoSQL  ## #
# client = pymongo.MongoClient("mongodb://admin:admin@127.0.0.1:27017/")
client = pymongo.MongoClient(os.getenv('NO_SQL_DATABASE_URL'))
no_sql_db = client.portit
