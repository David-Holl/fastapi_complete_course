from fastapi import FastAPI
from project_3.TodoApp.database import engine
import project_3.TodoApp.models as models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
