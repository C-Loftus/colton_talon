from talon import Context, Module, actions
import time
ctx = Context()
ctx.matches = """tag: user.controlTabsWithPedal
app: chrome
"""

ctx.settings["user.force_synchronous"] = False

#  functions to be overwritten based on the context
@ctx.action_class("user")
class Actions:

    # def left_right_down():
    #     """Left and Right pedal"""

    # def left_center_down():
    #     """Left and Center pedal"""

    # def center_right_down():
    #     """Center and Right pedal"""

    # def left_center_right_down():
    #     """Left, Center and Right pedal"""

    def left_down():
        """left pedal"""
        actions.key("ctrl-pageup")
        time.sleep(0.5)

    # def left_down():
    #     # """left pedal down"""

    def right_down():
        """right pedal"""
        actions.key("ctrl-pagedown")
        time.sleep(0.5)

    # def right_down():
    #     """right pedal down"""

    # def center_up():
    #     """center pedal"""

    # def center_down():

        
    # def held_left():
    #     """ called when the left pedal is held down"""

    def held_right():
        """ called when the right pedal is held down"""
        
