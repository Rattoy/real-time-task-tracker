from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud, models, scheduler

Base.metadata.create_all(bind=engine)


class TaskCreate(BaseModel):
    title: str
    description: str | None = None

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")
def startup_event():
    scheduler.start_scheduler()

@app.get("/")
def root():
    return {"message": "Task API is running!"}

@app.get("/tasks/read")
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.post("/tasks/create")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title, task.description)

@app.post("/tasks/{task_id}/update")
def update_task(task_id: int, task: TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task.title, task.description)

@app.put("/tasks/{task_id}/complete")
def complete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.complete_task(db, task_id)

@app.delete("/tasks/{task_id}/delete")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)


