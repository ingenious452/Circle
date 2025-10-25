import asyncio
from desktop_notifier import DesktopNotifier


async def send_notification(message: str) -> None:
    notifier = DesktopNotifier("Circle")
    await notifier.send("Reminder", message)




