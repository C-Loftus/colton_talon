from talon import Context, Module, actions, settings
import time

ctx = Context()
ctx.matches = """title: /pptx/
title: /PowerPoint/
"""

ctx.settings["user.oneActionPerPedalPress"] = False
ctx.settings["user.oneActionOnCenterPress"] = False





@ctx.action_class("user")
class Actions:
    def left_down():
        """Left pedal"""
        # un focus any edited text
        actions.key("escape:2")
        actions.key("down")
        time.sleep(0.5)

    def right_down():
        """Right pedal"""
        # un focus any edited text
        actions.key("escape:2")
        actions.key("up")
        time.sleep(0.5)

    def center_down():
        """center pedal"""
        actions.key("tab")
        time.sleep(0.5)


    def left_right_down():
        """Left and Right pedal"""


    def center_up():
        """center pedal"""

        
