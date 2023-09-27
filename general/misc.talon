mode: command
-

# pull all talon scripts:
#     user.system_command_nb("find ~/.talon/user -name .git -print -execdir git pull \;")

queer line: edit.delete_line()

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