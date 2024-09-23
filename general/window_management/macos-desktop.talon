os: mac

-

move left:
    sleep(.3)
    key(cmd-alt-shift-left)

move right:
    sleep(.3)
    key(cmd-alt-shift-right)


cleft:
    edit.extend_word_left()
    edit.delete()
    
last [<number_small>]:
    key(cmd-9)
    times = number_small or 1
    times = times - 1
    # print(times)
    sleep(.05)
    key("ctrl-pageup:{times}")

tab <number_small>:
    key("cmd-{number_small}")


page hunt [<user.text>]:
    key(cmd-f)
    sleep(.2)
    insert("{text}")
