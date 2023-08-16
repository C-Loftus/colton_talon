mode: command
title: /Excel/
-

settings():
    key_hold = 50

take <user.letter> <number>:
    key(ctrl-g)
    insert("{letter}{number}\n")

take  <user.letter> <number> past <user.letter> <number>:
    key(ctrl-g)
    insert("{letter}{number}:{letter_2}{number_2}")
    key(enter)

take until <user.letter> <number>:
    key(ctrl-g)
    insert("A1:{letter}{number}")
    key(enter)


select column:
    key(ctrl-shift-down)

select row:
    key(shift-space)

edit cell:
    key(f2)

show formulas:
    key(ctrl-~)

next sheet:
    key(ctrl-pagedown)

previous sheet:
    key(ctrl-pageup)

fit column:
    key(alt-h)
    key(o)
    key(i)

fit row:
    key(alt-h)
    key(o)
    key(a)

format currency: key(ctrl-shift-$)
format percent: key(ctrl-shift-%)
format date: key(ctrl-shift-#)
format time: key(ctrl-shift-@)
format scientific: key(ctrl-shift-^)
format number: key(ctrl-shift-!)
format strike: key(ctrl-5)
hints toggle: key(alt)

