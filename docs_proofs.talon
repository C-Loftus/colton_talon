title: /Google Docs/


-

settings():
    key_wait = 10.0

equation:
    key(alt-shift-i)
    key(e)

sigma <number> <number>:
    insert("\\sum ")
    insert(number)
    key(enter)
    user.paste("∞")
    key(enter)

sigma <number> infinity:
    insert("\\sum ")
    insert(number)
    key(enter)
    user.paste("∞")
    key(enter)

section:
    key(alt-shift-i)
    key(r)
divide:
    insert("\\frac ")
new proof:
    key(enter)
    key(enter)
    key(alt-shift-i)
    key(r)
    key(ctrl-shift-7)
    