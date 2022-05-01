mode: command
-

start meditation:
    user.system_command_nb("gnome-screensaver-command -a")

pull all talon scripts:
    user.system_command_nb("find ~/.talon/user -name .git -print -execdir git pull \;")