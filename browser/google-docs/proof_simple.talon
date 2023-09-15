
mode: command
title: /docs.google/

-


for all:
    insert('\\forall')
    key(space)
Special in:
    insert('\\in')
    key(space)
infinite:
    user.paste("∞")
    key(right)

Greater  equal:
    ">="
Less equal:
    "<="

bullet point:
    key(ctrl-shift-8)

indent right:
    key(ctrl-])
indent left:
    key(ctrl-[)
equation:
    key(alt-shift-i)
    sleep(.3)
    key(e)
divide:
    insert("\\frac ")

probability:
    insert("Pr[]")
    key(left)

expectation <user.letter>:
    insert("E[{letter}]")
    key(left)

expectation:
    insert("E[]")
    key(left)