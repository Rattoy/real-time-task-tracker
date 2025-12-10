from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database import SessionLocal, engine, Base
from app import crud, models, scheduler

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.on_event("startup")  # API calls the scheduler when the app starts
def startup_event():
    scheduler.start_scheduler()

@app.get("/") # Root endpoint to check if API is running
def root():
    return {"message": "Task API is running!"}

@app.get("/tasks/read") # Endpoint to read all tasks
def read_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db)


@app.post("/tasks/create") # Endpoint to create a new task
def create_task(task: models.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task.title, task.description)

@app.post("/tasks/{task_id}/update") # Endpoint to update an existing task
def update_task(task_id: int, task: models.TaskCreate, db: Session = Depends(get_db)):
    return crud.update_task(db, task_id, task.title, task.description)

@app.put("/tasks/{task_id}/complete") # Endpoint to mark a task as complete
def complete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.complete_task(db, task_id)

@app.delete("/tasks/{task_id}/delete") # Endpoint to delete a task
def delete_task(task_id: int, db: Session = Depends(get_db)):
    return crud.delete_task(db, task_id)


