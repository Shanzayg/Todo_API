from fastapi import FastAPI
from app.routers import todos, tasks

app = FastAPI()

app.include_router(
    todos.router,
    prefix="/todos",
    tags=["Todos"]
)
app.include_router(
    tasks.router,
    prefix="/tasks",
    tags=["Tasks"]
)


@app.get("/")
def home():
    return {"message": "Welcome to my Todo API"}