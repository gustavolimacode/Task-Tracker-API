from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.db.database import get_db
from app.schemas.task import TaskCreate, Task
from app.services.task_service import (
    list_tasks_service,
    create_task_service,
    mark_as_done_service,
    delete_task_service,
)

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/", response_model=List[Task])
def list_tasks(db: Session = Depends(get_db)) -> list[Task]:
    return list_tasks_service(db)

@router.post("/", response_model=Task)
def create_task(data: TaskCreate, db: Session = Depends(get_db)) -> Task:
    return create_task_service(data, db)

@router.patch("/{task_id}/done", response_model=Task)
def mark_as_done(task_id: int, db: Session = Depends(get_db)):
    return mark_as_done_service(task_id, db)

@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: int, db: Session = Depends(get_db)) -> Task:
    return delete_task_service(task_id, db)