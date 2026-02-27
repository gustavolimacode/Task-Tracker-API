from app.schemas.task import TaskCreate, Task
from fastapi import HTTPException
import app.database as db
from typing import List


def list_tasks_service() -> List[Task]:
    return db.tasks

def create_task_service(data: TaskCreate) -> Task:
    new_task = {
        "id": db.next_id,
        "title": data.title,
        "done": False
    }
    db.tasks.append(new_task)
    db.next_id += 1
    return new_task

def mark_as_done_service(task_id: int):
    for task in db.tasks:
        if task['id'] == task_id:
            if task['done']:
                raise HTTPException(status_code=400, detail="Task já foi concluída")
            task['done'] = True
            return {"message": "Task marcada como concluída"}
    raise HTTPException(status_code=404, detail="Task não encontrada")

def delete_task_service(task_id: int) -> Task:
    for i, task in enumerate(db.tasks):
        if task['id'] == task_id:
            db.tasks.pop(i)
            return task
    raise HTTPException(status_code=404, detail="Task não encontrada")