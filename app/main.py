import time # middleware
from fastapi import FastAPI, Request
from app.routers import todos, tasks
from app.config import settings  # for environment variables 
from app.database import engine, Base
from app import models

Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.APP_NAME)

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
    return {
        "message": "Welcome to my Todo API",
        "app_name": settings.APP_NAME,
        "debug": settings.DEBUG
    }

@app.middleware("http")
async def log_requests(request: Request, call_next):

    start_time = time.time()

    print(f"Request: {request.method} {request.url}")

    response = await call_next(request)

    process_time = time.time() - start_time

    print(f"Status code: {response.status_code}")
    print(f"Request processed in: {process_time:.4f} seconds")

    response.headers["X-Process-Time"] = str(process_time)

    return response