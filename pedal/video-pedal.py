from talon import Context, Module, actions
import time, random, math, os

ctx = Context()
ctx.matches = """title: /watch/
title: /soundcloud/
title: /Internet Archive/
"""

speed_mode = False

ctx.settings["user.force_synchronous"] = True

@ctx.action_class("user")
class Actions:

    def left_right_down():
        """Left and Right pedal"""
        print("speed mode")
        global speed_mode
        speed_mode = not speed_mode

    def left_up():
        # os.system("amixer -D pulse sset Master 5%- > /dev/null")
        if speed_mode:
            actions.key("s:3")
        else:
            actions.key("voldown")

    def right_up():
        # os.system("amixer -D pulse sset Master 5%+ > /dev/null")
        if speed_mode:
            actions.key("d:3")
        else:
            actions.key("volup")

    def center_up():
        actions.key("space")
        
