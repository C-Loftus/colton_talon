app: vscode
mode: command

-
new window:
    key(ctrl-shift-n)

focus lines:
    key(ctrl-shift-alt-d)


run python:
    key(ctrl-s)
    sleep(.1)
    key(ctrl-shift-alt-d)
    sleep(.1)
    key(ctrl-f10)

kill python:
    key(ctrl-shift-alt-f)
    sleep(.25)
    key(ctrl-c)

restart python:
    key(ctrl-shift-alt-f)
    sleep(.25)
    key(ctrl-c)
    key(ctrl-s)
    sleep(.1)
    key(ctrl-shift-alt-d)
    sleep(.1)
    key(ctrl-f10)

Run again:
    key(ctrl-shift-alt-f)
    sleep(.25)
    key(up)
    key(enter)

backup:
    key(ctrl-shift-alt-f)
    user.paste("fgc")
    key(enter)


print:
    insert('print()')
    key(left)

switch project:
    key(ctrl-r)
    sleep(0.25)
    key(enter)

special:
    "``"
    key(left:1)
    