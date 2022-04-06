title: /Google Docs/
mode: command

-
settings():
    key_wait = 10.0

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
    key(e)
divide:
    insert("\\frac ")

probability:
    insert("Pr[]")
    key(left)

expectation <user.letter>:
    insert("E[{letter}]")
    key(left)