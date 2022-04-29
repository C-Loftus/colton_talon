mode: command

-
jump firefox:
    key(alt-1)
    user.switcher_focus("firefox")
Jump code:
    key(alt-2)
    user.switcher_focus("code")

Left monitor:
    key(super-shift-left)

Right monitor:
    key(super-shift-right)

Shut down computer now:
    key(super-c)
    sleep(1)
    user.paste("shutdown now")

reset window tiling:
    key(super-r)
    sleep(.25)
    key(super-e)
    print("reset window tiling")

