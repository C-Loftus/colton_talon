mode: command
os: linux
-

Toggle stacking:
    key(super-s)
# stack left:
#     key(super-left)
# Switch stack right:
# key(super-right)

move <number_small>:
    key("alt-shift-{number_small}")

bounce <number_small>:
    key("alt-{number_small}")

focus left:
    key(super-left)

focus right:
    key(super-right)

Shut down computer now:
    key(super-c)
    sleep(1)
    user.paste("shutdown now")

reset window tiling:
    key(super-r)
    sleep(.25)
    key(super-e)
    print("reset window tiling")
