from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from circle.config import config
from circle.core.logger import logger
from circle.core.notification.base import Notification
from circle.core.notification.exceptions import NotificationError
from circle.core.notification.registry import register_channel


@register_channel("telegram")
class TelegramNotification(Notification):

    def __init__(self):
        self._logger = logger.get_logger("telegram", config.LOG_DIR/"notification.log")

    def send(self, title: str,  message: str) -> None:
        payload = urlencode({
            "chat_id": config.TELEGRAM_CHAT_ID,
            "text": f"{title}\n{message}"
        }).encode()
        try:
            request = Request(config.TELEGRAM_CHAT_URI, data=payload)
            with urlopen(request) as response:
                if response.getcode() == 200:
                    self._logger.info(f"notification sent")
                else:
                    self._logger.error(f"error sending notification: {response.getcode()}")
        except (HTTPError, URLError) as e:
            self._logger.exception(f"unexpected error sending notification: {e}")
            raise NotificationError(str(e))
