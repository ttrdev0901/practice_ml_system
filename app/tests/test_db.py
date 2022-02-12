from sqlalchemy import create_engine

# テスト対象
from app.db.initialize import create_tables

def test_db_create_tables():
    engine = create_engine("sqlite:///:memory:", echo=True)
    actual = create_tables(engine=engine)