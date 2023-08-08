from talon import Module, actions, cron, scope, Context, settings
import time

mod = Module()

map = {
    "left": False,
    "right": False,
    "center": False
}

#  By default  this is false which signifies a continuously called function 
# (Holding down scroll etc)
force_synchronous = mod.setting(
    "force_synchronous",
    type=bool,
    default=False, 
    desc="force_synchronous",
)

#  turns just the center pedal into a synchronous option
force_synchronous_center = mod.setting(
    "force_synchronous_center",
    type=bool,
    default=True,
    desc="force_synchronous_center",
)

pedal_scroll_amount=mod.setting(
    "pedal_scroll_amount",
    type=float,
    default=0.1,
    desc="pedal_scroll_amount",
)

ctx = Context()

def on_interval():

    # if map contains at least 2 true values, then we have a double keypress
    if two_keypress():

        if map["left"] and map["right"]:
            
            actions.user.left_right_down()
        elif map["left"] and map["center"]:
            actions.user.left_center_down()
        elif map["center"] and map["right"]:
            actions.user.center_right_down()
    
        reset_map()
        return  

    # with synchronous code we only call functions on the pedal up
    # pedal down functions  can be asynchronous and held down to repeat,
    #  which is impossible if we have to force synchronous
    if settings.get("user.force_synchronous"):
        return

    if map["center"] and not settings.get("user.force_synchronous_center"):
        actions.user.center_down()
    elif map["left"]:
        actions.user.left_down()
    elif map["right"]:
        actions.user.right_down()

reset_map = lambda: map.update({k: False for k in map.keys()})
two_keypress = lambda: sum(map.values()) >= 2

cron.interval("16ms", on_interval)


@mod.action_class
class Actions:

    def pedal_down(key: str):
        """Map the key name to down"""
        map[key]=True


    def pedal_up(key: str):
        """Pedal up"""
        # If you have a synchronous double keypress that has already reset the map, then we don't want to do anything. this prevents single actions mistakenly firing after the double action

        if map[key] == False:
            return
        else:
            map[key]=False

        #  if we have a  discrete action that needs to wait and can't be asynchronous, 
        # then we can't use the cron job and as a result we have to do it synchronously on the pedal raise.
        if settings.get("user.force_synchronous") == True:
            if key == "left":
                actions.user.left_up( )
            elif key == "right":
                actions.user.right_up( )
            elif key == "center":
                actions.user.center_up()

        elif settings.get("user.force_synchronous_center") == True:
            actions.user.center_up()

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
        actions.user.mouse_scroll_down(pedal_scroll_amount.get())

    def right_down():
        """Right pedal"""
        actions.user.mouse_scroll_up(pedal_scroll_amount.get())
    def center_down():
        """Center pedal"""


    # default implementations to override contextually
    def left_up():
        """Left pedal up"""
    def right_up():
        """Right pedal up"""
    def center_up():
        """Center pedal up"""
        modes = scope.get("mode")
        if "sleep" in modes:
            # mode = "sleep"
            actions.speech.enable()
        else:    
            actions.speech.disable()