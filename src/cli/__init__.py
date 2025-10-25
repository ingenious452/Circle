import typer
from src.cli import contact, daemon

app = typer.Typer()

app.command('start')

app.add_typer(contact.contact_app, name="contact")
app.add_typer(daemon.daemon_app, name="daemon")

