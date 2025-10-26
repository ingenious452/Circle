from notifypy import Notify

from circle.core.notification.base import Notification
from circle.core.notification.exceptions import NotificationError
from circle.core.notification.registry import register_channel

@register_channel("desktop")
class DesktopNotification(Notification):

    def send(self, title: str, message: str) -> None:
        try:
            notification = Notify(default_notification_application_name="CirCle",
                                  default_notification_icon=r"C:\Users\drkwo\Downloads\meme.png")
            notification.title = title
            notification.message = message
            notification.send()
        except Exception as e:
            raise NotificationError(str(e))
