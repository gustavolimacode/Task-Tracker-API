from fastapi import APIRouter

router = APIRouter(prefix="/tasks", tags=["tasks"])

@router.get("/")
def list_tasks():
    return {"message": "list_tasks has not yet been implemented"}

@router.post("/")
def create_task():
    return {"message": "create_task has not yet been implemented"}