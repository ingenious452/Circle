import typer
from . import add, delete, show, update

contact_app = typer.Typer(help="Manage Circle 🌀 contacts")

contact_app.command('add')(add.add_contact)
contact_app.command('delete')(delete.delete_contact)
contact_app.command('show')(show.show_contact)
contact_app.command('update')(update.update_contact)
