title: /Google Docs/
mode: command

-
# settings():
#     key_wait = 10.0




sigma:
    insert('\\sum \n')
    key(right)
alpha:
    insert('\\alpha ')
    key(space)
beta:
    insert('\\beta ')
    key(space)

gamma:
    insert('\\gamma ')
    key(space)
delta:
    insert('\\delta ')
    key(space)
epsilon:
    insert('\\epsilon ')
    key(space)

integral <user.alnum> <user.alnum>:
    insert("\\int {alnum_1}\n{alnum_2}\n")

sigma <user.alnum> <user.alnum>:
    insert("\\sum {alnum_1}\n{alnum_2}\n")

<user.alnum> choose <user.alnum>:
    insert("\\choose {alnum_1}\n{alnum_2}\n")

sigma (<number>|<user.letter>) infinity:
    insert("\\sum ")
    insert(number or letter)
    key(enter)
    insert("∞")
    key(enter)


<user.alnum> divide  <user.alnum>:
    insert("\\frac {alnum_1}\n{alnum_2}\n")
    

special <user.letters>:
    key(space)
    key(alt-shift-i)
    key(e)
    user.insert_formatted(letters, "ALL_CAPS")
    key(right)
    key(space)

special alpha:
    key(space)
    key(alt-shift-i)
    key(e)
    insert("\\alpha")
    key(space)
    key(right)

special beta:
    key(space)
    key(alt-shift-i)
    key(e)
    insert("\\beta")
    key(right)
    key(space)

special gamma:
    key(space)
    key(alt-shift-i)
    key(e)
    insert("\\gamma")
    key(right)
    key(space)

special delta:
    key(space)
    key(alt-shift-i)
    key(e)
    insert("\\delta")
    key(right)

special <user.letters> sub <number>:
    key(space)
    key(alt-shift-i)
    key(e)
    user.insert_formatted(letters, "ALL_CAPS")
    insert("_{number}")
    key(right)
    key(right)

special down <user.letters> sub <number>:
    key(space)
    key(alt-shift-i)
    key(e)
    insert(letters)
    insert("_{number}")
    key(right)
    key(right)


special down <user.letters>:
    key(alt-shift-i)
    key(e)
    insert(letters)
    key(right)

<user.letter> sub <number>:
    insert("{letter}_")
    insert("{number}")
    key(right)
<user.letter> sub <user.letter>:
    insert("{letter}_")
    insert("{letter_2}")
    key(right)

