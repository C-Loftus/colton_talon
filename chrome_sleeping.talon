# activate this .talon file if the current app name is "Chrome"
# you can find app names by running ui.apps() in the REPL
app.name: Google-chrome
mode: sleep

-

# disable dictation
parrot(lll):
    key(ctrl-shift-s)

dictate:
    key(ctrl-shift-s)
  
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
    key(ctrl-backspace)

parrot(palate_click):
    user.mouse_toggle_control_mouse()
    print("palate_click")

  