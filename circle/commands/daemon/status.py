import rich
from circle.core.daemon import get_daemon_manager


def daemon_status():
    manager = get_daemon_manager()
    status = manager.status()
    rich.print(f"daemon {status}")
