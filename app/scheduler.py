from apscheduler.schedulers.background import BackgroundScheduler
from crud import check_deadlines
from database import SessionLocal

sched = BackgroundScheduler()

def start_scheduler():
    sched.add_job(lambda: check_deadlines(next(iter(SessionLocal()))), 'interval', minutes=1)
    sched.start()
