import typer
from . import stop, start, status


app = typer.Typer(help="Manage Circle 🌀 daemon")

app.command('start')(start.start_daemon)
app.command('stop')(stop.stop_daemon)
app.command('status')(status.daemon_status)