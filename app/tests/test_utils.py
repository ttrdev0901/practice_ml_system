import pytest

from app.utils import database
from app.utils import config_reader

def test_utils_config_reader_db():
    expected = {
        "connector": "psycopg2",
        "hostname": "localhost",
        "username": "ml_app",
        "password": "password",
        "dbname": "mldb",
        "port": "5432"
    }

    actual = config_reader.read_db_config()

    assert expected == actual

def test_utils_database():
    expected = "postgresql+psycopg2://ml_app:password@localhost:5432/mldb"
    actual = database.get_db_url()

    assert expected == actual