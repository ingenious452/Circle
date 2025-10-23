import typer
from src.cli import daemon

app = typer.Typer()

app.command('start')

app.add_typer(daemon.daemon_app, name="daemon")


if __name__ == "__main__":
    app()
