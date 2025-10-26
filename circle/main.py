

# from circle.core.daemon import get_daemon_manager

import typer
from circle.commands import daemon, contact


app = typer.Typer()
app.add_typer(contact.app, name="contact")
app.add_typer(daemon.app, name="daemon")


# b = NotificationManager(channels=("desktop", "telegram"))
# b.notify("Birthday 🎂", "Wish happy birthday to my friend")


# from circle.core.daemon import get_daemon_manager
# a = get_daemon_manager()

if __name__ == "__main__":
    # c = DaemonManager(config.DAEMON_SCRIPT,
    #                   config.PID_FILE,
    #                   config.STOP_FILE,
    #                   config.LOG_DIR / "daemon.log")
    # print(a)
    # a.terminate()
    app(prog_name="circle")
    #
    # d = get_daemon_manager()