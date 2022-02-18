from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.db import cruds
from app.db import schemas

router = APIRouter()


@router.get("/projects/all")
def project_all(db: Session = Depends(get_db)):
    return cruds.selectProjectAll(db=db)

@router.get("/projects/name/{project_name}")
def project_by_name(project_name: str, db: Session=Depends(get_db)):
    return cruds.selectProjectByName(
                        db=db,
                        project_name=project_name
                    )

@router.post("/projects/")
def add_project(project: schemas.ProjectCreate, db=Depends(get_db)):
    return cruds.addProject(
        db=db,
        project=project
    )