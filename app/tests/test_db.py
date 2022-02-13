from sqlalchemy import create_engine

# テスト対象
from app.db.initialize import create_tables
from app.db.database import DBSettings
from app.db.cruds import (
    selectProjectAll,
    selectProjectByName,
    addProject
)

def test_db_create_tables():
    engine = create_engine("sqlite:///:memory:", echo=False)
    actual = create_tables(engine=engine)


def test_dbsettings():
    import os

    os.environ["hostname"] = "localhost" 
    os.environ["dbname"] = "mldb"
    os.environ["username"] = "ml_app"
    os.environ["password"] = "password"
    os.environ["port"] = "5432"
    os.environ["connector"] = "psycopg2"

    expected = ("postgresql+psycopg2://"
                "ml_app:password@localhost:5432/mldb")

    assert expected == DBSettings().get_uri()