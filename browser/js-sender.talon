# sends JS files to the browser

app: browser

-

browser send <user.talon_JS_Functions>:
    user.send_js(talon_JS_Functions)
    
key(ctrl-alt-5):
    user.build_js()    