from talon import Context, Module, actions, settings
import enum

ctx = Context()
ctx.matches = """
mode: command
title: /Excel/i
not app: vscode
title: /.xlsx/i
not app: vscode
"""

ctx.settings["user.force_synchronous"] = False

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
#Create an enumeration for either horizontal or vertical
SCROLL_DIRECTION = enum.Enum("SCROLL_DIRECTION", ["vertical", "horizontal"])
current_direction=SCROLL_DIRECTION.vertical


@ctx.action_class("user")
class Actions:

    def left_down():
        if not settings.get("user.force_synchronous"):
            if current_direction==SCROLL_DIRECTION.vertical:
                # actions.user.mouse_scroll_down(pedal_scroll_amount)
                actions.key("down")
            else:
                # actions.user.mouse_scroll_left(pedal_scroll_amount)
                actions.key("left")
    

    def right_down():
        if not settings.get("user.force_synchronous"):
            if current_direction==SCROLL_DIRECTION.vertical:
                # actions.user.mouse_scroll_up(pedal_scroll_amount)
                actions.key("up")

            else:
                # actions.user.mouse_scroll_right(pedal_scroll_amount)
                actions.key("right")

    def left_right_down():
        global current_direction
        print("Excel direction switched")
        
        match current_direction:
            case SCROLL_DIRECTION.vertical:
                current_direction = SCROLL_DIRECTION.horizontal
            case SCROLL_DIRECTION.horizontal:
                current_direction = SCROLL_DIRECTION.vertical
        
