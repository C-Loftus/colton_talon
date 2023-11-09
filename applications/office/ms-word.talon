title: /Word/
title: /.docx/

-

level <number_small>:
    key("alt-ctrl-{number_small}")

read aloud:
    key(f10)
    sleep(.2)
    key(w)
    sleep(.2)
    key(l)
    sleep(.2)
    key(2)
    sleep(.2)
    key(ctrl-alt-space)

bullet:  key(ctrl-.)

paste that:
    key(ctrl-shift-v)

new comment:                key(ctrl-alt-m)
new footnote:               key(alt-ctrl-f)

formatted footnote:
    key(alt-ctrl-f)
    sleep(.5)
    key(ctrl-shift-v)
    sleep(.5)
    key(escape)
    key(ctrl-shift-left)
    sleep(.5)
    key(ctrl-shift-+)
    key(right)

new end note:               key(alt-ctrl-d)
remove highlighting:
    key(alt-h)
    sleep(.1)
    key(i)
    sleep(.1)
    key(n)
clear formatting:           key(ctrl-space)

format strike through:      key(ctrl-shift-x)
