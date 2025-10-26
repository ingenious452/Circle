import typer
from . import add, delete, show, update

app = typer.Typer(help="Manage Circle 🌀 contacts")

app.command('add')(add.add_contact)
app.command('delete')(delete.delete_contact)
app.command('show')(show.show_contact)
app.command('update')(update.update_contact)
