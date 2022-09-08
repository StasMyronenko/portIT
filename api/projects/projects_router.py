from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from typing import List

from configuration.utils import get_db
from projects.projects_service import get_projects_list
from projects.schemas import ProjectBase

project_router = APIRouter()


@project_router.get("/", response_model=List[ProjectBase])
def projects_list(db: Session = Depends(get_db)):
    projects = get_projects_list(db)
    return projects
