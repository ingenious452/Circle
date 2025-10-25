
""" this will hold the reminder logic for my application.
I will create a scheduler application for each one of my reminder and save it.

"""
import sys
import time
from fileinput import filename

# import json
# import os
# import time
# from datetime import datetime
# from apscheduler.schedulers.background import BackgroundScheduler
# from apscheduler.triggers.cron import CronTrigger
# from apscheduler.triggers.date import DateTrigger
#
# DATA_DIR = os.path.join(os.path.dirname(__file__), "../data")
# REMINDERS_FILE = os.path.join(DATA_DIR, "reminders.json")
#
#
# # ----------------------------
# # Utilities
# # ----------------------------
# def load_json(file_path):
#     if not os.path.exists(file_path):
#         with open(file_path, "w") as f:
#             json.dump([], f)
#     with open(file_path, "r") as f:
#         return json.load(f)
#
#
# def save_json(file_path, data):
#     with open(file_path, "w") as f:
#         json.dump(data, f, indent=4)
#
#
# def notify_user(reminder):
#     print(f"🔔 Reminder: {reminder['message']}")
#     if reminder.get("repeat", "once").lower() == "once":
#         reminder["status"] = "done"
#         reminders = load_json(REMINDERS_FILE)
#         for r in reminders:
#             if r["id"] == reminder["id"]:
#                 r["status"] = "done"
#         save_json(REMINDERS_FILE, reminders)
#
#
# # ----------------------------
# # Scheduler
# # ----------------------------
# def schedule_reminder(scheduler, reminder):
#     repeat = reminder.get("repeat", "once").lower()
#     scheduled_dt = datetime.fromisoformat(reminder["scheduled_time"])
#
#     if repeat == "once":
#         trigger = DateTrigger(run_date=scheduled_dt)
#     elif repeat == "daily":
#         trigger = CronTrigger(hour=scheduled_dt.hour, minute=scheduled_dt.minute)
#     elif repeat == "weekly":
#         trigger = CronTrigger(day_of_week=scheduled_dt.weekday(), hour=scheduled_dt.hour, minute=scheduled_dt.minute)
#     elif repeat == "yearly":
#         trigger = CronTrigger(month=scheduled_dt.month, day=scheduled_dt.day,
#                               hour=scheduled_dt.hour, minute=scheduled_dt.minute)
#     else:
#         trigger = DateTrigger(run_date=scheduled_dt)
#
#     scheduler.add_job(
#         notify_user,
#         trigger=trigger,
#         args=[reminder],
#         id=f"reminder_{reminder['id']}",
#         replace_existing=True
#     )
#
#
# # ----------------------------
# # Load and Schedule All Reminders
# # ----------------------------
# def schedule_all():
#     scheduler = BackgroundScheduler()
#     scheduler.start()
#
#     reminders = load_json(REMINDERS_FILE)
#     for reminder in reminders:
#         if reminder.get("status", "pending") == "pending":
#             schedule_reminder(scheduler, reminder)
#             print(f"📅 Scheduled reminder: {reminder.get('title')} at {reminder['scheduled_time']}")
#
#     print("🌀 Reminder daemon running...")
#     try:
#         while True:
#             time.sleep(60)
#     except KeyboardInterrupt:
#         print("🛑 Daemon stopped.")
#         scheduler.shutdown()
#
#
# # ----------------------------
# # Run
# # ----------------------------
# if __name__ == "__main__":
#     schedule_all()

import logging
import asyncio
from os.path import exists

logger = logging.getLogger("daemon")

log_file = r"D:\Web_Development\kill_enemy\circle\circle_v1\logs\scheduler\reminder.log"

logger.setLevel(logging.INFO)

log_file_handler = logging.FileHandler(filename=log_file, mode="a", encoding="utf-8")
log_formatter = logging.Formatter("{asctime} - {levelname} - {message}",
                                  style="{",
                                  datefmt="%Y-%m-%d %H:%M",
                                )
log_file_handler.setFormatter(log_formatter)
logger.addHandler(log_file_handler)
def show_reminder(message):
    logger.info(f"Message: {message}")

# scheduler = BackgroundScheduler()

logger.warning("working")
# def start_scheduler():
#     print('executing')
#     logger.info("Daemon started... 👹")
#
#     # job_id = scheduler.add_job(show_reminder, 'interval', seconds=3, args=['hello'])
#     # job_id2 = scheduler.add_job(show_reminder, 'interval', seconds=2, args=['second hello'])
#     #
#     # scheduler.start()
#
# def stop_scheduler(signum, frame):
#     # if scheduler.running:
#     #     scheduler.shutdown()
#     logger.warning(f"Demon stopped... 👹 {signum}")
#
#     logger.warning("Demon stopped... 👹")
#
# signal.signal(signal.SIGTERM, stop_scheduler)
# signal.signal(signal.SIGINT, stop_scheduler)
#
# def scheduler_status():
#     # status = "running" if scheduler.running else "stopped"
#     logger.info(f"Daemon status: running ")
#
# # circle/daemon/runner.py
# def handle_signal(signum, frame):
#     logger.warning("shutting down daemon")
#     # sys.exit(0)

# scheduler_process.py
import time
import signal
import datetime
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from notification import send_notification

running = True
# scheduler = AsyncIOScheduler()

def example_job():
    logger.info(f"[Job] Reminder fired at {datetime.datetime.now()}")

def handle_signal(signum, frame):
    logger.warning(f"[Signal] Caught {signum}, stopping...")
    # scheduler.shutdown(wait=False)

def stop_scheduler(signum, frame):
    # if scheduler.running:
    #     scheduler.shutdown()
    logger.warning(f"Demon stopped... 👹 {signum}")




# def main():
#     # signal.signal(signal.SIGTERM, handle_signal)
#     signal.signal(signal.SIGINT, handle_signal)
#     scheduler.add_job(send_notification, "interval", seconds=5, args=["What do you think of this async"])
#     logger.info("[Scheduler] Starting...")
#
#     try:
#         scheduler.start()
#
#     except (KeyboardInterrupt, SystemExit):
#         logger.info("[Scheduler] Exiting gracefully.")
import asyncio
import os
import sys
import time
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from pathlib import Path
# from logger import logger # Assuming you have a logger configured

# --- Configuration ---
BASE_DIR = Path().absolute().parent.parent
STOP_FILE = BASE_DIR / "circled.stop"
PID_FILE = BASE_DIR / "circled.pid"

# Event to signal the main loop to stop
stop_event = asyncio.Event()


async def check_stop_file():
    while not stop_event.is_set():
        if STOP_FILE.exists():
            stop_event.set()
            logger.info("Stop file found stopping gracefully")
            return
        await  asyncio.sleep(1)


def main():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    ascheduler = AsyncIOScheduler(event_loop=loop)


    ascheduler.add_job(send_notification, 'interval', seconds=10, args=["My async function"])

    stop_checker_task = loop.create_task(check_stop_file())
    logger.info(f"[Scheduler] started. PID: {os.getpid()}")
    ascheduler.start()

    try:
        loop.run_until_complete(stop_event.wait())
    except KeyboardInterrupt:
        pass
    finally:
        ascheduler.shutdown(wait=False)
        stop_checker_task.cancel()
        PID_FILE.unlink()
        STOP_FILE.unlink()
        loop.close()
        logger.info("[Scheduler] gracefully stopped and loop closed.")

if __name__ == "__main__":
    main()
