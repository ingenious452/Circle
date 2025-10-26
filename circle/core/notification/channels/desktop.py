import random

from notifypy import Notify

from circle.config import config
from circle.core.logger import logger
from circle.core.notification.base import Notification
from circle.core.notification.exceptions import NotificationError
from circle.core.notification.registry import register_channel


@register_channel("desktop")
class DesktopNotification(Notification):

    def __init__(self):
        self._logger = logger.get_logger("desktop", config.LOG_DIR/"notification.log")

    def send(self, title: str, message: str) -> None:
        try:
            icon_path = config.ICONS["cloud"] if config.ICONS else None
            notification = Notify(default_notification_application_name="Circle",
                                  default_notification_icon=icon_path)
            notification.title = title
            notification.message = message
            notification.send()
            self._logger.info(f"successfully sent notification!")
        except Exception as e:
            self._logger.exception(f"unexpected error sending notification: {e}")
            raise NotificationError(str(e))
