from circle.core.daemon import get_daemon_manager


def stop_daemon():
    manager = get_daemon_manager()
    manager.terminate()
