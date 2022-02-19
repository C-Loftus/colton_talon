title: /Google Docs/
mode: command


-
settings():
    key_wait = 10.0

    
bullet point:
    key(ctrl-shift-8)

indent right:
    key(ctrl-])
indent left:
    key(ctrl-[)
equation:
    key(alt-shift-i)
    key(e)

sigma <number> <user.letter>:
    insert("\\sum ")
    insert(number)
    key(enter)
    insert(letter)
    key(enter)

infinite:
    user.paste("∞")
    key(right)

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

<number> divide <number>:
    insert("\\frac ")
    insert(number)
    key(right)
    insert(number_2)
    key(right)

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
    
expectation <user.letter>:
    insert("E[{letter}]")
    key(left)

<user.letter> sub <number>:
    insert("{letter}_")
    insert("{number}")
    key(right)
<user.letter> sub <user.letter>:
    insert("{letter}_")
    insert("{letter_2}")
    key(right)

disclaimer:
    user.paste('Please note I have an ODS medical exemption as a result of hand issues.  Any differences such as hand written solutions or formatting irregularities caused by voice dictation are due to this')
    sleep(.5)
    key(alt-shift-i)
    sleep(.5)
    key(r)