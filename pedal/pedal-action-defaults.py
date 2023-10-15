from talon import Module, actions, scope, Context, settings

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

pedal_scroll_amount=mod.setting(
    "pedal_scroll_amount",
    type=float,
    default=0.1,
    desc="pedal_scroll_amount",
)
teamNotOutlook=False


# default implementations to override contextually
@mod.action_class
class Actions:


    def left_center_right_down():
        """Left, Center and Right pedal"""

    def center_right_down():
        """Center and Right pedal"""
        ctx.settings['user.pedal_scroll_amount'] = 0.2
        print("Speed reset to 0.2")


    def left_right_down():
        """Left and Right pedal"""
        ctx.settings['user.pedal_scroll_amount'] = settings.get("user.pedal_scroll_amount")
        ctx.settings['user.pedal_scroll_amount']+=0.2
        print(f'Speed set to: {ctx.settings["user.pedal_scroll_amount"]}')

    def left_center_down():
        """Left and Center pedal"""


    def left_down():
        """Left pedal"""
        actions.user.mouse_scroll_down(settings.get("user.pedal_scroll_amount"))

    def right_down():
        """Right pedal"""
        actions.user.mouse_scroll_up(settings.get("user.pedal_scroll_amount"))
    def center_down():
        """Center pedal"""
        # modes = scope.get("mode")
        # if "sleep" in modes:
        #     # mode = "sleep"
        #     actions.speech.enable()
        # else:    
        #     actions.speech.disable()
        # time.sleep(2)

    def left_up():
        """Left pedal up"""
    def right_up():
        """Right pedal up"""
    def center_up():
        """Center pedal up"""
        actions.user.toggle_sleep_mode()
    
    def held_left():
        """ called when the left pedal is held down"""
        if "user.tabsWithPedal" in list(ctx.tags):
            ctx.tags = []
        else:
            ctx.tags = ["user.controlTabsWithPedal"]
    def held_right():
        """ called when the right pedal is held down"""
    def held_center():
        """ called when the right pedal is held down"""
        print("Held center")
        chrome = actions.user.get_running_app("Chrome")
        actions.user.switcher_focus_app(chrome)
        global teamNotOutlook
        if teamNotOutlook:
            actions.key("ctrl-shift-6")
        else:
            actions.key("ctrl-shift-7")
        teamNotOutlook = not teamNotOutlook

        
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