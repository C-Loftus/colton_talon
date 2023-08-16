os: windows
mode: command

-

target teams:
    chrome = user.get_running_app("Chrome")
    user.switcher_focus_app(chrome)
    key(ctrl-shift-6)

target mail:
    chrome = user.get_running_app("Chrome")
    user.switcher_focus_app(chrome)
    key(ctrl-shift-7)