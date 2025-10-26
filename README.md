# Circle 🌀
A birthday reminder application.

Having issue while creating a daemon service
I am not able to terminate the process of daemon after it is executed

1. success in creating a demon process and getting it's process id
2. terminate the daemon - successfully stopping daemon but it is still not showing any message
3. show daemon status


I need to create a reminder daemon service that will check the reminder and schedule a notification whenever
it is due.

for that I need to create a daemon
How?
what is a daemon service is a background service that run along
with your application and does some task for you and it closes whenever the parent process
closes but
I want a daemon service that not only run in background but does not close even if the parent closes

using `subprocess` module I can do that.

Now for scheduling task I need to use `apscheduler` library to create a scheduling job

so what is async- 

it is that cpu is not waiting for a task to be completed and thread is alway
executing the next avaialbe task .

a couroutine is async def and await is used to tell the event loop that it is waiting for the task to complete

scheduling and Daemon are working as expected 

we need to fine tune stop and show functionality

I need to be able to add reminder to scheduler for yearly monthly or daily
all these reminder must me saved somewhere in the application


circle reminder  add <name> --date 06/13 --type 'brithday'
circle reminder view <name> --all
circle reminder delete <name> 
circle reminder update <name>


circle contact add <name> --date 06/13
circle contact view <name> --all
circle contact delete <name>
circle contact update <name>

crcle daemon start
circle reminder start
circle reminder stop
circle reminder status

each contact will have a reminder or multiple reminders one to many relationship


# what new or better thing I learn
1. module and packages are namespaces so when 

> the reason when uv run circle/main.py is executed we get import error for `from circle.core import daemon` is because
> python is taking `circle/` as the root directory of the project and when it sees circle.core it assumes there is another
> folder named circle in the current working directory but there isn't any so we get `Module not found error` and when you run it as
> packager the `sys.path`  or `python`  put the current directory `.` as the directory path so it look into the current directory instead
> of `circle/` and voila :) everything works!



2. How closure works
> these are basically function that are defined inside another function and according to python name sapce rules

[Builtin Box]   ← Python’s internal memory (e.g., len, print, sum)
     ↑
[Global Box]    ← Variables defined at top level of your file
     ↑
[Enclosing Box] ← Outer function’s memory
     ↑
[Local Box]     ← Current function’s memory


```python
def something_fun(message):
     print(message)

     def other_fun(outside_fun):
       print(outside_fun)
         
    return other_fun  # return a decorator function

@something_fun('helo')   # this is immediately calling something func as we normally would   
# therefore this function must return a decorator (A function that take another function as an argument)
class NameFunnyShit:
    def __init__(self, *values):
        print(values)
```


## Problem: daemon is not workin
1. I am able to run the process from my script but the typer module is not able to run the program

> solved: the problme was module resolution I was trying to run the daemon as a script which should have been a 
> run as a package using the infamous `m`

### Problem : my env file was not laoding the bot token for telegram

1. the problem was that when we run the code as module the configuration .env load doesn't work 

to fix: we have to load env using absolute path 
> Reasoning (short): when you run code as a module or from a different launcher, the current working directory (cwd) and sys.path differ from when you run a script from the project root. python-dotenv's load_dotenv/find_dotenv by default looks relative to the cwd (or uses find_dotenv which searches up from cwd). If the daemon starts with a different cwd or environment, load_dotenv won't locate your .env and TELEGRAM_BOT_TOKEN will be empty → chat_uri built without token