from fastapi import APIRouter, HTTPException, status, Depends

router = APIRouter()

tasks = [
    {"id": 1, "title": "Learn FastAPI"},
    {"id": 2, "title": "Practice Python"}
]

def find_task(task_id: int):

    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Task not found"
    )

@router.get("/")
def get_task():
    return tasks


@router.get("/{task_id}")
def get_task(task = Depends(find_task)):
    return task