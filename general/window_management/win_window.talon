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


exit user session:
    user.notify("shutting down")
    sleep(8)
    user.system_command("shutdown /s /t 0")
