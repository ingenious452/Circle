from typing import List, Optional
from .exceptions import NotificationError
from circle.core.logger import get_logger
from circle.core.config import config

from circle.core.notification.registry import CHANNEL_REGISTRY as CHANNELS

logger = get_logger("notification", config.LOG_DIR / 'notifier.log')


class NotificationManager:
    """
    Notifier class to handle sending notification to user channels
    """
    def __init__(self, channels: Optional[List[str]] = None) -> None:
        # Check what has been passed is a list of single object
        self._channels = self._init_channel(channels or [])
        logger.debug(f"Initialized with channels: {[c.__class__.__name__ for c in self._channels]}")

    @staticmethod
    def _init_channel(channel_names: List[str]):
        notifiers = []
        for channel_name in channel_names:
            channel_cls = CHANNELS.get(channel_name)
            if channel_cls is None:
                logger.warning(f"Invalid channel '{channel_name}' ignored.")
                continue
            try:
                notifiers.append(channel_cls())
            except Exception as e:
                logger.error(f"Failed to initialize channel '{channel_name}': {e}")
        return notifiers

    def notify(self, title, message: str, channels: Optional[List[str]] = None) -> None:
        target_channels = (
            self._init_channel(channels) if channels else self._channels
        )
        for channel in target_channels:
            try:
                channel.send(title, message)
                logger.info(f'Sent message via {channel.__class__.__name__} successfully!')
            except NotificationError as e:
                logger.error(f'Error sending {channel.__class__.__name__} message: {e}')
            except Exception as e:
                logger.exception(f"Unexpected error in {channel.__class__.__name__}: {e}")
