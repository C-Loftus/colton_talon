mode: command

-

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

