from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.types import JSON
from sqlalchemy import create_engine

from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.functions import current_timestamp

# --------------
# 自作モジュール
# --------------
from app.utils import database

Base = declarative_base()

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(
                    String(255),
                    primary_key=True,
                    comment="主キー"
                )
    project_name = Column(
                    String(255),
                    nullable=False,
                    unique=True,
                    comment="プロジェクト名"
                )
    description = Column(
                    Text,
                    nullable=True,
                    comment="説明"
                )
    created_datetime = Column(
                    DateTime(timezone=True),
                    server_default=current_timestamp(),
                    nullable=False
                )

class Model(Base):
    __tablename__ = "models"

    model_id = Column(
                    String(255),
                    primary_key=True,
                    comment="主キー"
                )
    project_id = Column(
                    String(255),
                    ForeignKey("projects.project_id"),
                    nullable=False,
                    comment="外部キー: projects.project_id"
                )
    model_name = Column(
                    String(255),
                    nullable=False,
                    comment="モデル名"
                )   
    description = Column(
                    Text,
                    nullable=True,
                    comment="説明"
                )
    created_datetime = Column(
                    DateTime(timezone=True),
                    server_default=current_timestamp(),
                    nullable=False
                )

class Experiment(Base):
    __tablename__ = "experiments"

    experiment_id = Column(
        String(255),
        primary_key=True,
        comment="主キー"
    )
    model_id = Column(
        String(255),
        ForeignKey("models.model_id"),
        nullable=False,
        comment="外部キー: models.model_id"
    )
    model_version_id = Column(
        String(255),
        nullable=False,
        comment="モデルの実験バージョンID"
    )
    parameters = Column(
        JSON,
        nullable=True,
        comment="学習パラメータ"
    )
    training_dataset = Column(
        Text,
        nullable=True,
        comment="学習データ"
    )
    validation_dataset = Column(
        Text,
        nullable=True,
        comment="検証データ"
    )
    test_dataset = Column(
        Text,
        nullable=True,
        comment="テストデータ"
    )
    evaluations = Column(
        JSON,
        nullable=True,
        comment="評価結果"
    )
    artifact_file_path = Column(
        Text,
        nullable=False,
        comment="モデルファイルのパス"
    )
    created_datetime = Column(
        DateTime(timezone=True),
        server_default=current_timestamp(),
        nullable=False
    )