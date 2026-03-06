from fastapi import APIRouter
from app.schemas.task import TaskCreate, Task
import app.database as db
from typing import List
from app.services.task_service import (
    create_task_service,
    list_tasks_service,
    mark_as_done_service,
    delete_task_service,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
def list_tasks() -> list[Task]:
    return list_tasks_service()

@router.post("/", response_model=Task)
def create_task(data: TaskCreate) -> Task:
    return create_task_service(data)

@router.patch("/{task_id}/done", response_model=Task)
def mark_as_done(task_id: int):
    return mark_as_done_service(task_id)

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int) -> Task:
    return delete_task_service(task_id)