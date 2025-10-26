from circle.core.notification.base import Notification
from typing import Dict, Type


CHANNEL_REGISTRY:Dict[str, Type[Notification]] = {}


def register_channel(channel_name: str):
    def wrapper(channel_class: Type[Notification]) -> Type[Notification]:
        CHANNEL_REGISTRY[channel_name] = channel_class
        return channel_class
    return wrapper


