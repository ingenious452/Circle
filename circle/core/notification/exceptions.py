class NotificationError(Exception):
    """Base exception for all notification-related errors."""
    def __init__(self, message: str, *, channel: str | None = None):
        super().__init__(message)
        self.channel = channel

    def __str__(self):
        base = super().__str__()
        return f"[{self.channel.upper()}] {base}" if self.channel else base


class ChannelNotFoundError(NotificationError):
    """Raised when the requested notification channel does not exist."""
    pass


class NotificationSendError(NotificationError):
    """Raised when sending a notification fails."""
    def __init__(self, message: str, *, channel: str | None = None, cause: Exception | None = None):
        super().__init__(message, channel=channel)
        self.cause = cause


class NotificationConfigError(NotificationError):
    """Raised when notification configuration (API key, etc.) is invalid."""
    pass


class NotificationPermissionError(NotificationError):
    """Raised when a user or system denies notification permission."""
    pass
