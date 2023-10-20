# sends JS files to the browser

tag: browser

-

user script <user.talon_JS_Functions>:
    user.notify("Sending JS files to browser")
    key("ctrl-shift-j")
    sleep(1)
    user.copy_js("{user.talon_JS_Functions}")
    key(ctrl-v)
    sleep(0.5)
    key(enter)
    sleep(1)
    key(ctrl-shift-j)

help user script:
    user.help_list("user.talon_JS_Functions")