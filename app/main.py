from fastapi import FastAPI


from app.api.routers import projects
from app.db.database import engine
from app.db.database import SessionLocal
from app.db.initialize import create_tables

create_tables(engine=engine)

app = FastAPI()


app.include_router(projects.router)