from talon import Context, Module, actions

ctx = Context()
ctx.matches = """title:  
title: 
"""

ctx.settings["user.oneActionPerPedalPress"] = False

#  functions to be overwritten based on the context
@ctx.action_class("user")
class Actions:

    def east_west_down():
        """Left and Right pedal"""

    def left_center_down():
        """Left and Center pedal"""

    def center_east_down():
        """Center and Right pedal"""

    def east_north_west_down():
        """Left, Center and Right pedal"""

    def west_up():
        """left pedal"""

    def west_down():
        """left pedal down"""

    def east_up():
        """right pedal"""
    def east_down():
        """right pedal down"""

    def north_up():
        """center pedal"""

    def held_north():
        """called when the center pedal is held down"""
    def held_west():
        """ called when the left pedal is held down"""
    def held_east():
        """ called when the right pedal is held down"""
        
