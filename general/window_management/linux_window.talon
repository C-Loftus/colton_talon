mode: command
os: linux
-

focus <user.running_applications>: 
    user.jump_workspace_and_switch_focus(running_applications)
Toggle stacking:
    key(super-s)
# stack left:     
#     key(super-left)
# Switch stack right:     
    # key(super-right)

move <number_small> :
    key("alt-shift-{number_small}")

bounce <number_small> :
    key("alt-{number_small}")



move left:
    key(super-shift-left)

move right:
    key(super-shift-right)

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

