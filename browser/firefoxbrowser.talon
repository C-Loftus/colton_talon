app: firefox

-

# vimium requirement
split new window:
    key(shift-w)

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
