from talon import Context, Module, actions, settings
import time

ctx = Context()
ctx.matches = """title: /pptx/
"""

ctx.settings["user.force_synchronous"] = False

@ctx.action_class("user")
class Actions:
    def left_down():
        """Left pedal"""
        actions.key("down")
        time.sleep(0.5)

    def right_down():
        """Right pedal"""
        actions.key("up")
        time.sleep(0.5)

    def left_right_down():
        """Left and Right pedal"""


    def center_up():
        """center pedal"""

        
