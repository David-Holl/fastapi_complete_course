from fastapi import FastAPI
from project_3.TodoApp.database import engine
from project_3.TodoApp.database import Base
from project_3.TodoApp.routers import admin, auth, todos, users

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/healthy")
def health_check() -> dict[str, str]:
    return {"status": "healthy"}


app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)
