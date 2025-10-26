import rich

from circle.core.daemon import get_daemon_manager


manager = get_daemon_manager()


def daemon_status():
    status = manager.status()
    rich.print(f"[Daemon] - [yellow]{status}[/yellow]")
