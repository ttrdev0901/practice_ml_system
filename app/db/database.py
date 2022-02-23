from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from pydantic import BaseSettings

class DBSettings(BaseSettings):
    dbhost: str
    dbname: str
    dbuser: str
    dbpassword: str
    dbport: int
    dbconnector: str

    def get_uri(self):
        return (f"postgresql+{self.dbconnector}://"
                f"{self.dbuser}:{self.dbpassword}@{self.dbhost}:{self.dbport}/{self.dbname}")



#  参考: https://fastapi.tiangolo.com/ja/tutorial/sql-databases/
engine = create_engine(
    url=DBSettings().get_uri()
    # url='sqlite:///./sqlite.db'
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



