app: Kitty

-

update system:
    "sudo apt update; sudo apt upgrade"

search for [{user.letter}]:
    insert('grep -ri {user.letter}' or 'grep -ri')

copy that:  
    key(ctrl-shift-c)

paste that:
    key(ctrl-shift-v)