from fastapi import FastAPI
from app.routes.tasks import router as task_routes
from app.db.database import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Task Tracker API", version="0.2.0")

@app.get("/health")
def health_check():
    return {"message": "ok"}

app.include_router(task_routes)