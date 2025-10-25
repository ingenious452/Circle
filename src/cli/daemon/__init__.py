import typer
from . import stop, start, status


daemon_app = typer.Typer(help="Manage Circle 🌀 daemon")

daemon_app.command('start')(start.start_daemon)
daemon_app.command('stop')(stop.stop_daemon)
daemon_app.command('status')(status.daemon_status)