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

ctx.settings["user.oneActionPerPedalPress"] = False
ctx.settings["user.oneActionOnCenterPress"] = False

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
#Create an enumeration for either horizontal or vertical
SCROLL_DIRECTION = enum.Enum("SCROLL_DIRECTION", ["vertical", "horizontal"])
current_direction=SCROLL_DIRECTION.vertical


@ctx.action_class("user")
class Actions:

    # def west_down():
    #     actions.key("ctrl-enter")
    #     if not settings.get("user.oneActionPerPedalPress"):
    #         if current_direction==SCROLL_DIRECTION.vertical:
    #             # actions.user.mouse_scroll_down(pedal_scroll_amount)
    #             actions.key("down")
    #         else:
    #             # actions.user.mouse_scroll_left(pedal_scroll_amount)
    #             actions.key("left")
    #     actions.sleep(0.8)
    def west_down():
        # actions.key("ctrl-enter")
        actions.key('left')
        actions.sleep(0.2)
    
    def north_down():
        # actions.key("ctrl-enter")
        actions.key('up')
        actions.sleep(0.2)
    
    def south_down():
        # actions.key("ctrl-enter")
        actions.key('down')
        actions.sleep(0.2)

    def east_down():
        # actions.key("ctrl-enter")
        actions.key('right')
        actions.sleep(0.2)

    # def east_down():
        
    #     actions.key("ctrl-enter")

    #     if not settings.get("user.oneActionPerPedalPress"):
    #         if current_direction==SCROLL_DIRECTION.vertical:
    #             # actions.user.mouse_scroll_up(pedal_scroll_amount)
    #             actions.key("up")

    #         else:
    #             # actions.user.mouse_scroll_right(pedal_scroll_amount)
    #             actions.key("right")
    #     actions.sleep(0.8)

    # def east_west_down():
    #     global current_direction
    #     print("Excel direction switched")
        
    #     match current_direction:
    #         case SCROLL_DIRECTION.vertical:
    #             current_direction = SCROLL_DIRECTION.horizontal
    #         case SCROLL_DIRECTION.horizontal:
    #             current_direction = SCROLL_DIRECTION.vertical
        
