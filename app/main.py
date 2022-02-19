import os
os.environ["hostname"] = "localhost" 
os.environ["dbname"] = "mldb"
os.environ["username"] = "ml_app"
os.environ["password"] = "password"
os.environ["port"] = "5432"
os.environ["connector"] = "psycopg2"


from fastapi import FastAPI


from app.api.routers import projects
from app.db.database import engine
from app.db.database import SessionLocal
from app.db.initialize import create_tables

create_tables(engine=engine)

app = FastAPI()


app.include_router(projects.router)