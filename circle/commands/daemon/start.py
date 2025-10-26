from circle.core.daemon import get_daemon_manager


def start_daemon():
    manager = get_daemon_manager()
    manager.start()
