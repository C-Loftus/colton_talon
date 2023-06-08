mode: command

-
system monitor:
    key(super-c)
    sleep(1.3)
    insert("htop")

    key(enter)
launch code dotfiles:
    user.system_command_nb("code ~/dotfiles")
launch code:
    user.system_command_nb("code")
launch code thesis:
    user.system_command_nb("code ~/Projects/thesis")
Launch code voice: 
    user.system_command_nb("code ~/numen")

launch code data:
    user.system_command_nb("code ~/SCh")

launch chrome:
    user.system_command_nb("google-chrome")

launch code talon:
    user.system_command_nb("code ~/.talon/user")

launch code independent:
    user.system_command_nb("code ~/Projects/newIWVoice")

launch kitty:
    user.system_command_nb("kitty")

launch firefox:
    user.system_command_nb("firefox")
launch dot files:
    user.system_command_nb("code ~/dotfiles")