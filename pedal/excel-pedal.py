from talon import Context, Module, actions, settings
import enum

ctx = Context()
ctx.matches = """
title: /Excel/i
title: /.xlsx/
"""

ctx.settings["user.force_synchronous"] = False

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
#Create an enumeration for either horizontal or vertical
SCROLL_DIRECTION = enum.Enum("SCROLL_DIRECTION", "vertical", "horizontal")
scroll_direction=SCROLL_DIRECTION.vertical


@ctx.action_class("user")
class Actions:

    def left_down():
        if not settings.get("user.force_synchronous"):
            if scroll_direction==SCROLL_DIRECTION.vertical:
                actions.user.mouse_scroll_down(pedal_scroll_amount)
            else:
                actions.user.mouse_scroll_left(pedal_scroll_amount)
    

    def right_down():
        if not settings.get("user.force_synchronous"):
            if scroll_direction==SCROLL_DIRECTION.vertical:
                actions.user.mouse_scroll_up(pedal_scroll_amount)
            else:
                actions.user.mouse_scroll_right(pedal_scroll_amount)

    def left_right_down():
        global scroll_direction
        
        if scroll_direction == SCROLL_DIRECTION.vertical:
            scroll_direction = SCROLL_DIRECTION.horizontal
        else:
            scroll_direction = SCROLL_DIRECTION.vertical

        
