from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models.task import Task
from app.schemas.task import TaskCreate


def list_tasks_service(db: Session):
    return db.query(Task).all()

def create_task_service(data: TaskCreate, db: Session):
    new_task = Task(title=data.title, done=False)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def mark_as_done_service(task_id: int, db: Session):
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    if task.done:
        raise HTTPException(status_code=400, detail="Task is already marked as done")
    
    task.done = True
    db.commit()
    db.refresh(task)
    
    return task


def delete_task_service(task_id: int, db: Session) -> Task:
    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    db.delete(task)
    db.commit()
    
    return task