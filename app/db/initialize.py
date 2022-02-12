from app.db.models import Base

def create_tables(engine):
    """データベースにテーブルを作成する

    Parameters
    ----------
    engine : sqlalchemy.engine
        データベースへの接続エンジン
    """
    Base.metadata.create_all(bind=engine, checkfirst=True)