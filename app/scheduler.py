from apscheduler.schedulers.background import BackgroundScheduler
import datetime

scheduler = BackgroundScheduler()

def print_heartbeat():
    print("Scheduler is alive:", datetime.datetime.now())

def start_scheduler():
    scheduler.add_job(print_heartbeat, "interval", seconds=10)
    scheduler.start()
