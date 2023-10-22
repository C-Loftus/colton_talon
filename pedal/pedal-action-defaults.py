from talon import Module, actions, scope, Context, settings
from .pedal_types import AppToActivate

mod = Module()
ctx = Context()
ctx.tags = []
mod.tag("controlTabsWithPedal", desc="tag for controlling tabs with pedal")

#  By default  this is false which signifies a continuously called function 
# (Holding down scroll etc)
mod.setting(
    "oneActionPerPedalPress",
    type=bool,
    default=False, 
    desc="If a pedal is held down, only fire the action once.   In other words only trigger the pedal up action once.",
)

#  turns just the center pedal into a synchronous option
# This defaults true so we can use the center pedal for things like toggling Talon sleep versus Talon wake
#  where we don't want it to repeat
mod.setting(
    "oneActionOnCenterPress",
    type=bool,
    default=True,
    desc="If specifically the center pedal is held down, only fire the action once.   In other words only trigger the pedal up action once.",
)

mod.setting(
    "pedal_scroll_amount",
    type=float,
    default=0.1,
    desc="pedal_scroll_amount",
)

mod.setting(
    'secondsToTriggerPedalHold',
    type=int,
    default=2,
    desc='secondsToTriggerPedalHold',
)

holdTriggerApp = AppToActivate.MICROSOFT_TEAMS


# default implementations to override contextually
@mod.action_class
class Actions:


    def east_north_west_down():
        """Left, Center and Right pedal"""

    def center_east_down():
        """Center and Right pedal"""
        ctx.settings['user.pedal_scroll_amount'] = 0.2
        print("Speed reset to 0.2")


    def east_west_down():
        """Left and Right pedal"""
        ctx.settings['user.pedal_scroll_amount'] = settings.get("user.pedal_scroll_amount")
        ctx.settings['user.pedal_scroll_amount']+=0.2
        print(f'Speed set to: {ctx.settings["user.pedal_scroll_amount"]}')

    def left_center_down():
        """Left and Center pedal"""


    def west_down():
        """Left pedal"""
        actions.user.mouse_scroll_down(settings.get("user.pedal_scroll_amount"))

    def east_down():
        """Right pedal"""
        actions.user.mouse_scroll_up(settings.get("user.pedal_scroll_amount"))
    def north_down():
        """Center pedal"""
        # modes = scope.get("mode")
        # if "sleep" in modes:
        #     # mode = "sleep"
        #     actions.speech.enable()
        # else:    
        #     actions.speech.disable()
        # time.sleep(2)

    def west_up():
        """Left pedal up"""
    def east_up():
        """Right pedal up"""
    def north_up():
        """Center pedal up"""
        actions.user.toggle_sleep_mode()
    
    def held_west():
        """ called when the left pedal is held down"""
        if "user.controlTabsWithPedal" in list(ctx.tags):
            ctx.tags = []
        else:
            ctx.tags = ["user.controlTabsWithPedal"]
        actions.user.notify('controlling tabs')

    def held_east():
        """ called when the right pedal is held down"""
    def held_north():
        """ called when the right pedal is held down"""
        print("Held center")
        chrome = actions.user.get_running_app("Chrome")
        actions.user.switcher_focus_app(chrome)

        global holdTriggerApp
        match holdTriggerApp: 
            case AppToActivate.MICROSOFT_TEAMS:
                actions.key("ctrl-shift-6")
                holdTriggerApp = AppToActivate.MICROSOFT_OUTLOOK
            case AppToActivate.MICROSOFT_OUTLOOK:
                actions.key("ctrl-shift-7")
                holdTriggerApp = AppToActivate.MICROSOFT_TEAMS
            case _:
                raise ValueError(f"AppToActivate is of type {type(holdTriggerApp)} but must be within {AppToActivate}")
        
    def toggle_tab_mode():
        """called when the center pedal is held down"""
        if "user.tabsWithPedal" in list(ctx.tags):
            ctx.tags = []
        else:
            ctx.tags = ["user.controlTabsWithPedal"]

    def reset_pedal_state():
        """"""
        ctx.tags = []
        ctx.settings['user.pedal_scroll_amount'] = 0.1