from fastapi.testclient import TestClient
from app.main import app
import app.database as db

client = TestClient(app)

def setup_function():
    db.tasks = []
    db.next_id = 1 

def test_create_task():
    response = client.post("/tasks/", json={"title": "Estudar FastAPI"})

    assert response.status_code == 200

    data = response.json()

    assert data['title'] == "Estudar FastAPI"
    assert data['id'] == 1
    assert data['done'] is False

def test_list_tasks():
    client.post("/tasks/", json={"title": "Task 1"})
    client.post("/tasks/", json={"title": "Task 2"})

    response = client.get("/tasks/")

    assert response.status_code == 200

    data = response.json()

    assert len(data) == 2

def test_delete_task():
    client.post("/tasks/", json={"title": "task 1"})
    client.post("/tasks/", json={"title": "task 2"})
    client.post("/tasks/", json={"title": "task 3"})

    response = client.delete("/tasks/3")

    assert response.status_code == 200

    deleted_task = response.json()
    assert deleted_task['id'] == 3
    
    list_response = client.get("/tasks/")
    assert len(list_response.json()) == 2
    assert all(task['id'] != 3 for task in list_response.json())

def test_delete_task_not_found():
    client.post("/tasks/", json={"title": "task 1"})

    response = client.delete("/tasks/999")

    assert response.status_code == 404
    assert response.json()['detail'] == "Task não encontrada"

def test_mark_as_done():

    client.post("/tasks/", json={"title": "Task 1"})

    response = client.patch("/tasks/1/done")

    assert response.status_code == 200

    data = response.json()

    assert data['title'] == 'Task 1'
    assert data['id'] == 1
    assert data['done'] is True

    list_response = client.get("/tasks/")
    tasks = list_response.json()
    
    assert tasks[0]['done'] is True

def test_mark_as_done_already_done():
    client.post("/tasks/", json={"title": "Task 1"})

    first_response = client.patch("/tasks/1/done")
    assert first_response.status_code == 200

    response = client.patch("/tasks/1/done")

    assert response.status_code == 400
    assert response.json()['detail'] == "Task já foi concluída"