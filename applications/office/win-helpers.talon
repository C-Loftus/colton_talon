os: windows
-

# We don't have a guarantee that the item will be correctly orders
#  so we just approximate the location and that the user has to press enter
copy path:
    key(ctrl-l)
    sleep(.1)
    key(ctrl-c)
    key(escape)
    user.notify(clip.text())

close <user.running_applications>:
    user.switcher_focus(running_applications)
    sleep(.4)
    key(alt-f4)
