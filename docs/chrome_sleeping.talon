# activate this .talon file if the current app name is "Chrome"
# you can find app names by running ui.apps() in the REPL
app.name: Google-chrome

mode: sleep

-

# # disable dictation
# parrot(lll):
#     key(ctrl-shift-s)

listen:
    key(ctrl-shift-s)

mute:
    key(ctrl-shift-s)
    sleep(1)
    key(ctrl-backspace)
  
enter:
    key(enter)

down:
    key(down)

up:
    key(up)

left:
    key(left)

right:
    key(right)

left <digits>:
    key("left:{digits_1}")
right <digits>:
    key("right:{digits_1}")
down <digits>:
    key("down:{digits_1}")
up <digits>:
    key("up:{digits_1}")

backspace:
    key(backspace)

delete:
    sleep(.5)
    key(ctrl-backspace)


  