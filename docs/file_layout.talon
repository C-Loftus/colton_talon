title: /Google Docs/
mode: command

-
settings():
    key_wait = 10.0

disclaimer:
    'Please note I have an ODS medical exemption as a result of hand issues.  Any differences such as hand written solutions or formatting irregularities caused by voice dictation are due to this'
    sleep(.5)
    key(alt-shift-i)
    sleep(.5)
    key(r)

new proof <number>:
    key(enter)
    key(alt-shift-i)
    key(r)
    key(ctrl-alt-3)
    insert("Problem {number}")
    key(enter)

new part <user.letter>:
    key(enter)
    key(alt-shift-i)
    key(r)
    key(ctrl-alt-3)
    insert("Part {letter}")
    key(enter)

section:
    key(alt-shift-i)