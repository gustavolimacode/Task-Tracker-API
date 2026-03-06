import app.database as db
import pytest
from fastapi import HTTPException
from app.schemas.task import TaskCreate
from app.services.task_service import (
    list_tasks_service,
    create_task_service,
    mark_as_done_service,
    delete_task_service
)


def setup_function():
    """
    Essa função roda automaticamente antes de CADA teste deste arquivo.
    Ela garante que o "banco" em memória comece sempre limpo.
    """
    db.tasks = []
    db.next_id = 1

def test_create_task_service():
    # Arrange (preparação)
    data = TaskCreate(title="Aprender FastAPI")

    # Act (ação)
    created = create_task_service(data)

    # Assert (verificação)
    assert created['id'] == 1
    assert created['title'] == "Aprender FastAPI"
    assert created['done'] is False
    assert len(db.tasks) == 1
    assert db.tasks[0] == created
    assert db.next_id == 2

def test_list_tasks_service():
    # Arrange
    create_task_service(TaskCreate(title="Task 1"))
    create_task_service(TaskCreate(title="Task 2"))
    create_task_service(TaskCreate(title="Task 3"))

    # Act
    tasks = list_tasks_service()

    # Assert
    assert isinstance(tasks, list)
    assert len(tasks) == 3

    assert tasks[0]['id'] == 1
    assert tasks[0]['title'] == "Task 1"
    assert tasks[0]['done'] is False

    assert tasks[1]['id'] == 2
    assert tasks[1]['title'] == "Task 2"
    assert tasks[1]['done'] is False

    assert tasks[2]['id'] == 3
    assert tasks[2]['title'] == "Task 3"
    assert tasks[2]['done'] is False

def test_delete_task_service():
    # Arrange
    create_task_service(TaskCreate(title="Task 1"))
    create_task_service(TaskCreate(title="Task 2"))
    create_task_service(TaskCreate(title="Task 3"))

    # Act
    deleted = delete_task_service(2)

    # Assert
    assert len(db.tasks) == 2
    assert all(task['id'] != 2 for task in db.tasks)
    assert deleted['id'] == 2
    assert deleted['title'] == "Task 2"
 
def test_mark_as_done_service():
    # Arrange
    create_task_service(TaskCreate(title="Task 1"))

    # Act
    concluded = mark_as_done_service(1)

    # Assert
    assert len(db.tasks) == 1
    assert concluded['id'] == 1
    assert concluded['title'] == 'Task 1'
    assert concluded['done'] is True

def test_mark_as_done_already_done():
    # Arrange    
    create_task_service(TaskCreate(title="Task 1"))
    mark_as_done_service(1)

    # Act
    with pytest.raises(HTTPException) as exc_info:
        mark_as_done_service(1)

    # Assert
    assert len(db.tasks) == 1
    assert exc_info.value.status_code == 400
    assert exc_info.value.detail == "Task já foi concluída"
    assert db.tasks[0]['done'] is True