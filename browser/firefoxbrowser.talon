#My additional  commands for firefox beyond those in knausj

app: firefox

-
web search <user.text>:
    key(ctrl-t)
    key(ctrl-l)
    sleep(.05)
    insert(text)
    key(enter)

page hunt <user.text>:
    key(ctrl-f)
    sleep(.2)
    insert(text)

close tab:
    key(ctrl-w)
# vimium requirement
split window:
    key(shift-w)
# yo: 
#     key(f)
restore tab:
    key(X)

bookmark <user.word>:
    key(ctrl-b)
    sleep(.2)
    insert(user.word)

bookmarks:
    key(ctrl-b)
