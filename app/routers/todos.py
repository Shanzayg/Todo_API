from fastapi import APIRouter, HTTPException, status

router = APIRouter()

todos = [
    {"id": 1, "title": "Learn FastAPI"},
    {"id": 2, "title": "Learn SQL"},
    {"id": 3, "title": "Practice Python"}
]


@router.get("/")
def get_todos():
    return todos


@router.get("/{todo_id}")
def get_todo(todo_id: int):

    for todo in todos:
        if todo["id"] == todo_id:
            return todo

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Todo not found"
    )