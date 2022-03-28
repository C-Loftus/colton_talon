mode: command

-
system monitor:
    key(super-c)
    sleep(1.3)
    insert("htop")

    key(enter)

launch slack talon:
    user.system_command_nb("google-chrome https://app.slack.com/client/T7FPSMV8F/C7ENXA7C4")

launch code:
    user.system_command_nb("code")

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