mode: command
title: /Excel/i
not app: vscode
title: /.xlsx/i
not app: vscode
-

settings():
    key_hold = 50

take <user.excel_cell>:
    key(ctrl-g)
    insert("{excel_cell}\n")

change <user.excel_cell>:
    key(ctrl-g)
    key(enter)
    key(backspace)

take  <user.excel_cell> past <user.excel_cell>: 
    key(ctrl-g)
    insert("{user.excel_cell}:{user.excel_cell_2}")
    key(enter)

take until <user.excel_cell>: 
    key(ctrl-g)
    insert("A1:{user.excel_cell}")
    key(enter)


take column:
    key(ctrl-shift-down)

copy column:
    key(ctrl-shift-down)
    key(ctrl-c)



carve column:
    key(ctrl-shift-down)
    key(ctrl-x)

take row:
    key(shift-space)

copy row:
    key(shift-space)
    key(ctrl-c)

carve row:
    key(shift-space)
    key(ctrl-x)

edit cell:
    key(f2)

show formulas:
    key(ctrl-~)

next sheet:
    key(ctrl-pagedown)

previous sheet:
    key(ctrl-pageup)

fit column:
    key(alt-h)
    key(o)
    key(i)

fit row:
    key(alt-h)
    key(o)
    key(a)

format currency: key(ctrl-shift-$)
format percent: key(ctrl-shift-%)
format date: key(ctrl-shift-#)
format time: key(ctrl-shift-@)
format scientific: key(ctrl-shift-^)
format number: key(ctrl-shift-!)
format strike: key(ctrl-5)
hints toggle: key(alt)

new column:
    key(right)
    key(ctrl-shift-+)
    key(down:3)
    key(enter)

(new row | neuro):
    key(ctrl-shift-+)
    key(down:2)
    key(enter)

model fix this:
    key(ctrl-c)
    clipped = clip.text()
    delimRes = user.gpt_fix_delimited(clipped, "_")
    key(right)
    key(ctrl-shift-+)
    key(down:3)
    key(enter)
    user.paste_delimited(delimRes, "_", "column")


chuck this:
    key(ctrl--)
    key(enter)


copy append:
    mouse_click(0)
    text = clip.text()
    key(ctrl-c)
    clip.set_text("{text}\n{clip.text()}")