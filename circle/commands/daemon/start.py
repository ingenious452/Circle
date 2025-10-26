from circle.core.daemon import get_daemon_manager

import rich
manager = get_daemon_manager()


def start_daemon():
    rich.print(f"[Daemon] - [green]started[/green] 👹...")
    manager.start()
