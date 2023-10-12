# title: /.pptx/
# title: /PowerPoint/
tag: browser
-

^grab screen clip$:
    key(f11)
    sleep(6)
    user.screenshot_clipboard()
    key(f11)
^grab screen <number_small> clip$:
    #user.screenshot_clipboard(number_small)
^grab window clip$:
    #user.screenshot_clipboard()
    key(f11)
    sleep(6)
    user.screenshot_window_clipboard()
    key(f11)