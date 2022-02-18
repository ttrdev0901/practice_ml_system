from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseSettings

class DBSettings(BaseSettings):
    hostname: str
    dbname: str
    username: str
    password: str
    port: int
    connector: str

    def get_uri(self):
        return (f"postgresql+{self.connector}://"
                f"{self.username}:{self.password}@{self.hostname}:{self.port}/{self.dbname}")

#  参考: https://fastapi.tiangolo.com/ja/tutorial/sql-databases/
engine = create_engine(
    url=DBSettings().get_uri()
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally:
        db.close()



