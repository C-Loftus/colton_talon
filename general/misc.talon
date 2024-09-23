mode: command

-

# used for cursorless chaining
ergo:
    skip()

(fly | why):
    key(end)

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

(colgap | call gap):
    ": "

pad {user.symbol_key}:          " {symbol_key} "  

spam:
    ", "

alpha:
    user.paste("α")

beta:
    user.paste("β")


