## TEMPLATE used for creating new pedal scopes

from talon import Context, Module, actions

ctx = Context()
ctx.matches = """title:  
title: 
"""

ctx.settings["user.force_synchronous"] = False

@ctx.action_class("user")
class Actions:

    def left_right_down():
        """Left and Right pedal"""

    def left_up():
        """left pedal"""

    def right_up():
        """right pedal"""


    def center_up():
        """center pedal"""

        
