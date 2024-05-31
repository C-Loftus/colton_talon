import math
import os
import random
import time

from talon import Context, Module, actions

ctx = Context()
ctx.matches = """title: /watch/
title: /soundcloud/
title: /Internet Archive/
title: /linkedin.com/learning/i
title: /listen.overdrive.com/
"""

speed_mode = False

ctx.settings["user.oneActionPerPedalPress"] = True


@ctx.action_class("user")
class Actions:

    def east_west_down():
        """Left and Right pedal"""
        print("speed mode")
        global speed_mode
        speed_mode = not speed_mode

    def west_up():
        # os.system("amixer -D pulse sset Master 5%- > /dev/null")
        if speed_mode:
            actions.key("s:3")
        else:
            actions.key("voldown")

    def east_up():
        # os.system("amixer -D pulse sset Master 5%+ > /dev/null")
        if speed_mode:
            actions.key("d:3")
        else:
            actions.key("volup")

    def north_up():
        actions.key("space")
