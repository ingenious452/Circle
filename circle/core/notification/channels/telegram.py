from urllib.request import Request, urlopen
from urllib.parse import urlencode
from urllib.error import HTTPError, URLError

from circle.core.notification.base import Notification
from circle.core.config import config
from circle.core.notification.exceptions import NotificationError
from circle.core.notification.registry import register_channel

@register_channel("telegram")
class TelegramNotification(Notification):

    def send(self, title,  message: str) -> None:
        telegram_bot_url = f"https://api.telegram.org/bot{config.BOT_TOKEN}/sendMessage"
        payload = urlencode({
            "chat_id": config.CHAT_ID,
            "text": f"{title}\n{message}"
        }).encode()

        try:
            request = Request(telegram_bot_url, data=payload)
            with urlopen(request) as response:
                if response.getcode() == 200:
                    print('Telegram message sent successfully')
                else:
                    print(f'Telegram responded with code: {response.getcode()}')
        except (HTTPError, URLError) as e:
            raise NotificationError(str(e))
