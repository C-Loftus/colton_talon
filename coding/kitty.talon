app: Kitty
mode: command
os: linux

-

fill:
    key(ctrl-f)
    key(enter)
install:
    " sudo apt install"
update:
    " sudo apt update"

remove: 
    " sudo apt remove"
shortcut:
    " sudo apt update; sudo apt upgrade"

search for:
    insert('grep -ri "" *') 
    key(left:3)

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
    user.paste(" | kitty +kitten clipboard")

directory:
    user.paste(" mkdir ")

