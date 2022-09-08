from sqlalchemy.orm import Session
from projects.models import Project


def get_projects_list(db: Session):
    projects = db.query(Project).all()
    return projects
