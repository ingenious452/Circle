import time

from apscheduler.schedulers.background import BackgroundScheduler

import logging

from circle.core import config


from circle.core.logger import get_logger
from circle.core.config import config
from circle.core.notification.manager import NotificationManager

# Logger config
logger = get_logger("daemon", config.LOG_DIR / 'daemon.log')

scheduler = BackgroundScheduler()

event = "Meetings"
message = "hello go meet me!!!"

notification_manager = NotificationManager()

scheduler.add_job(notification_manager.notify, 'interval', seconds=5, args=[event, message, ("desktop", "telegram")])
scheduler.start()

def main():
    try:
        while True:
            if config.STOP_FILE.exists():
                logger.info("Stop file found, initiating graceful termination ;)")
                break
            time.sleep(1)
    except KeyboardInterrupt as e:
        pass
    finally:
        if scheduler.running:
            scheduler.shutdown(wait=False)
        try:
            # Use missing_ok=True for robust, non-crashing cleanup
            config.PID_FILE.unlink(missing_ok=True)
            config.STOP_FILE.unlink(missing_ok=True)
            logger.info("[Daemon] Control files removed.")
        except Exception as e:
            logger.warning(f"[Daemon] Failed to remove control files: {e}")
        logger.info("Circled terminated successfully, No further notification will be sent!")


if  __name__ == "__main__":
    main()
