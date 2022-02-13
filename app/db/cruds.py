import uuid
from sqlalchemy.orm import Session
from typing import List
from . import schemas
from . import models

def selectProjectAll(db: Session) -> List[schemas.Project]:
    """プロジェクト一覧を取得する関数

    Parameters
    ----------
    db : Session
        DB接続のセッション

    Returns
    -------
    List[schemas.Project]
        プロジェクト一覧のリスト
    """
    return db.query(models.Project).all()

def selectProjectByName(db: Session, project_name: str) -> schemas.Project:
    """指定したproject_nameのプロジェクトを取得する関数

    Parameters
    ----------
    db : Session
        [description]
    project_id : uuid.UUID
        [description]

    Returns
    -------
    schemas.Project
        [description]
    """
    return db.query(models.Project).filter(models.Project.project_name == project_name).first()

def addProject(db: Session, project: schemas.ProjectCreate) -> schemas.Project:
    """プロジェクトをデータベースに登録する関数

    Parameters
    ----------
    db : Session
        [description]
    project : schemas.ProjectCreate
        [description]

    Returns
    -------
    schemas.Project
        [description]
    """
    exist_project = selectProjectByName(db=db, project_name=project.project_name):
    
    if exist_project:
        return exist_project
    
    else:
        data = models.Project(
            project_id=str(uuid.uuid4()),
            project_name=project.project_name,
            description=project.description,
        )
        db.add(data)
        db.commit()
        db.refresh(data)
        return data

