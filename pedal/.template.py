from talon import Context, Module, actions

ctx = Context()
ctx.matches = """title:  
title: 
"""

ctx.settings["user.force_synchronous"] = False

#  functions to be overwritten based on the context
@ctx.action_class("user")
class Actions:

    def left_right_down():
        """Left and Right pedal"""

    def left_center_down():
        """Left and Center pedal"""

    def center_right_down():
        """Center and Right pedal"""

    def left_center_right_down():
        """Left, Center and Right pedal"""

    def left_up():
        """left pedal"""

    def left_down():
        """left pedal down"""

    def right_up():
        """right pedal"""
    def right_down():
        """right pedal down"""

    def center_up():
        """center pedal"""

    def held_center():
        """called when the center pedal is held down"""
    def held_left():
        """ called when the left pedal is held down"""
    def held_right():
        """ called when the right pedal is held down"""
        
