mode: command
-
route <user.text>:
    user.open_url("127.0.0.1:8000/{text}")

route switch <user.text>:
    key(ctrl-l)
    key(end)
    key(ctrl-backspace)
    insert("{text}")
    key(enter)

jump chrome:
    chrome = user.get_running_app("Chrome")
    user.switcher_focus_app(chrome)
    key(ctrl-shift-r)
