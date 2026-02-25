from fastapi import FastAPI
from app.routes.tasks import router as task_routes

app = FastAPI(title="Task Tracker API", version="0.1.0")

@app.get("/health")
def health_check():
    return {"message": "ok"}

app.include_router(task_routes)