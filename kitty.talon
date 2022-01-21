app: Kitty

-

update:
    "sudo apt update; sudo apt upgrade"

search for [{user.letter}]:
    insert('grep -ri {user.letter}' or 'grep -ri')

copy that:  
    key(ctrl-shift-c)

paste that:
    key(ctrl-shift-v)

split:
    key(ctrl-shift-enter)

new tab:
    key(ctrl-shift-t)

next tab:
    key(ctrl-shift-right)

copy to clipboard:
    user.paste("| kitty +kitten clipboard")