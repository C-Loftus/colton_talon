#My additional  commands for firefox beyond those in knausj

app: firefox

-
web search <user.text>:
    key(ctrl-l)
    sleep(.05)
    insert(text)
    key(enter)

close tab:
    key(ctrl-w)
# vimium requirement
split window:
    key(shift-w)
yo: 
    key(f)
restore tab:
    key(X)

bookmark <user.word>:
    key(ctrl-b)
    sleep(.2)
    insert(user.word)
search <user.word>:
    key(ctrl-f)
    sleep(.2)
    insert(user.word)

bookmarks:
    key(ctrl-b)
