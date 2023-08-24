#My additional  commands for firefox beyond those in knausj

tag: browser
# app: chrome

-
# for fire fox it requires my extension to switch to last tab with ctrl-9

last [<number_small>] :

    key(ctrl-9)
    times = number_small or 1
    times = times - 1
    # print(times)
    sleep(.05)
    key("ctrl-pageup:{times}")

tab <number_small> :
    key("ctrl-{number_small}")

web search [<user.text>]:
    key(ctrl-t)
    key(ctrl-l)
    sleep(.05)
    insert("{text}")

page hunt [<user.text>]:
    key(ctrl-f)
    sleep(.2)
    insert("{text}")

close tab:
    key(ctrl-w)
# vimium requirement
split window:
    key(shift-w)

restore tab:
    key(X)

bookmark <user.word>:
    key(ctrl-b)
    sleep(.2)
    insert(user.word)

bookmarks:
    key(ctrl-b)

pick <number_small>: 
    key("down:{number_small}") 
    key(enter)


notion save:
    key(ctrl-shift-k)
    sleep(1.5)
    key(enter)
    key(escape)


hence (toggle | switch): user.rango_command_without_target("toggleHints")