

# from circle.core.daemon import get_daemon_manager
# daemon_manager = get_daemon_manager()
#
#
# daemon_manager.terminate()


# # daemon_manager.start()
# daemon_manager.terminate()
# import typer
# from circle.commands import contact, daemon
# from circle.core.notification import get_notifier, get_notifiers
from circle.core.notification.manager import NotificationManager
from circle.core.notification.registry import CHANNEL_REGISTRY as CHANNELS
from circle.core.notification.channels.desktop import DesktopNotification

DesktopNotification()

# app = typer.Typer()
#
# app.command('start')

# print(CHANNELS)
# app.add_typer(contact.app, name="contact")
# app.add_typer(daemon.app, name="daemon")
# # a = get_notifiers(['desktop', 'telegram'])
b = NotificationManager(channels=("desktop", "telegram"))


b.notify("Birthday 🎂", "Wish happy birthday to my friend")


# checking what the scope resolution order in python is
# from pprint import pprint
# x = 12
# pprint(f"Global namespace: {dir()}")
#
# def update_x():
#     print("decorating something functional")
#     global x
#     x += 5  # raises UnboundLocalError
#     # other = 1
#     pprint(f"Value of x is: {x}")
#     pprint(f"Enclosing namespace: {dir()}")
#
#     def update_in_x():
#         # some_other = 12
#         # print(hoin)
#         # # y += 4
#         # print(f"other value is: {other}")
#         pprint(f"local namespace: {dir()}")
#     return update_in_x
#
# ghost = update_x()
# print("running outside>>>>>>")
# ghost()

#
#
# @update_x
# class NewCamel:
#     def __init__(self):
#         self.h = 12
#
#     def ok(self):
#         print(self.h)
#


# #
#
#
# if __name__ == "__main__":
#     app(prog_name="circle")
