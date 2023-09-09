mode: command
os: windows
-

focus <user.running_applications>: user.switcher_focus(running_applications)


move left:
    key(super-shift-left)

move right:
    key(super-shift-right)

snap right:
    key(super-right) 

snap left:
    key(super-left)

maximize:
    key(super-up)

# target {user.website}: user.open_or_focus_tab(website)

key(delete):
    key(voldown)

# key():
#     key(volup)

exit session now:
    key(ctrl-alt-t)
    sleep(2)
    user.paste("Stop-Computer -Force")
    key(enter)
