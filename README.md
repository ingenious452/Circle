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
