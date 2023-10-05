# sends JS files to the browser

tag: browser

-

user script <user.talon_JS_Functions>:
    user.notify("Sending JS files to browser")
    key("ctrl-shift-i")
    sleep(0.2)
    user.copy_js("{user.talon_JS_Functions}")
    key(ctrl-v)
    sleep(2)
    key(enter)
    sleep(2)
    key(ctrl-shift-i)

help user script:
    user.help_list("user.talon_JS_Functions")