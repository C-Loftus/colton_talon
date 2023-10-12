mode: command
-

# pull all talon scripts:
#     user.system_command_nb("find ~/.talon/user -name .git -print -execdir git pull \;")

target {user.website}:
    user.launch_new_tab_if_not_opened("{website}")

queer line: edit.delete_line()

inter:
    key(enter)

fly:
    key(end)

bullet:
    "* "

voyage: 
    key(volup:3)

vacate: 
    key(voldown:3)

smile:
    key(volup)

    
frown:
    key(voldown)

^thumbs up$:
    user.paste("👍")


scope: 
    user.paste("{\n\n}") 
    key(up)


colgap:
    ": "

^and$:
    key(end)

cycle results:
    #we don't have loops so we just have to repeat. easier than using pythonfor this small example
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)
    key(enter)
    sleep(2)

# copy path:
    # shift right click

    