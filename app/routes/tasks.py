from fastapi import APIRouter
from app.schemas.task import TaskCreate, Task
import app.database as db

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
def list_tasks():
    return db.tasks

@router.post("/", response_model=Task)
def create_task(data: TaskCreate):
    new_task = {
        "id": db.next_id,
        "title": data.title,
        "done": False
    }
    db.next_id += 1
    db.tasks.append(new_task)
    return new_task