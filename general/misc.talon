mode: command
-

# pull all talon scripts:
#     user.system_command_nb("find ~/.talon/user -name .git -print -execdir git pull \;")

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


hooks:
    insert("()")
    key(left)
scope: 
    user.paste("{\n\n}") 
    key(up)

^box$:
    user.paste("[]")
    key(left)
^skis$: 
    user.paste("``")
    key(left)

# fishes:
#     user.paste("<>")
#     key(left)

colgap:
    ": "

^diamond$:
    user.paste("<>")
    key(left)