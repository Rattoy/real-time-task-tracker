from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from crud import get_tasks, create_task, update_task, delete_task
from pydantic import BaseModel
import datetime
import scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()
scheduler.start_scheduler()

class TaskCreate(BaseModel):
    title: str
    description: str
    deadline: datetime.datetime

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/tasks/")
def add_task(task: TaskCreate, db: Session = Depends(get_db)):
    return create_task(db, task)

@app.get("/tasks/")
def list_tasks(db: Session = Depends(get_db)):
    return get_tasks(db)

@app.put("/tasks/{task_id}")
def update_task_status(task_id: int, done: bool, db: Session = Depends(get_db)):
    return update_task(db, task_id, done)

@app.delete("/tasks/{task_id}")
def remove_task(task_id: int, db: Session = Depends(get_db)):
    return delete_task(db, task_id)
