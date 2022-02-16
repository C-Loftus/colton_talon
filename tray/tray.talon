mode: command

-
start tray process:
    user.system_command_nb("python3 ~/.talon/user/myScripts/tray/indicator.talonSkip.py") 

start usage timer:
    user.socket_send("start timer")

stop usage timer:
    user.socket_send("stop timer")