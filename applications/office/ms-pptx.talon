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

^grab fast window clip$:
    user.screenshot_window_clipboard()

format black:
    user.rango_run_action_on_reference("clickElement", "black")
    sleep(6.5)
    user.rango_run_action_on_reference("clickElement", "color")
    key(escape)