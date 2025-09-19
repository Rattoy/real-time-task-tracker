from sqlalchemy.orm import Session
from app import models

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, title: str, description: str = None):
    task = models.Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def complete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.done = True
        db.commit()
        db.refresh(task)
    return task
def delete_task(db: Session, task_id: int):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        task.description = "Deleted"
        db.delete(task)
        db.commit()
    return task
def update_task(db: Session, task_id: int, title: str = None, description: str = None):
    task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if task:
        if title is not None:
            task.title = title
        if description is not None:
            task.description = description
        db.commit()
        db.refresh(task)
    return task