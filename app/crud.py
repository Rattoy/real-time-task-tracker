from sqlalchemy.orm import Session
from models import Task
import datetime

def get_tasks(db: Session):
    return db.query(Task).all()

def create_task(db: Session, task):
    db_task = Task(title=task.title, description=task.description, deadline=task.deadline)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, task_id: int, done: bool):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        task.done = done
        db.commit()
        db.refresh(task)
    return task

def delete_task(db: Session, task_id: int):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task:
        db.delete(task)
        db.commit()
    return task

def check_deadlines(db: Session):
    now = datetime.datetime.utcnow()
    tasks = db.query(Task).filter(Task.done==False).all()
    for task in tasks:
        if task.deadline <= now:
            print(f"⚠ Task {task.title} is overdue!")
