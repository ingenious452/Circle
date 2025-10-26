import rich

from circle.core.daemon import get_daemon_manager


manager = get_daemon_manager()


def stop_daemon():
    manager.terminate()
    rich.print("[Daemon] - [red]terminated[/red]")

