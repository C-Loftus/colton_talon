from talon import Module, actions, cron, scope, Context
import time


mod = Module()

map = {
    "left": False,
    "right": False,
    "center": False
}

force_synchronous = mod.setting(
    "force_synchronous",
    type=bool,
    default=False,
    desc="force_synchronous",
)
pedal_scroll_amount=mod.setting(
    "pedal_scroll_amount",
    type=float,
    default=0.2,
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

    if force_synchronous.get() == True:
        return

    elif map["left"]:
        actions.user.left_down()
    elif map["right"]:
        actions.user.right_down()
    elif map["center"]:
        actions.user.center_down()


reset_map = lambda: map.update({k: False for k in map.keys()})
two_keypress = lambda: sum(map.values()) >= 2

cron.interval("16ms", on_interval)



@mod.action_class
class Actions:

    def pedal_down(key: str):
        """Pedal down"""
        map[key]=True


    def pedal_up(key: str):
        """Pedal up"""
        # If you have a synchronous double keypress that has already reset the map, then we don't want to do anything. this prevents single actions mistakenly firing after the double action
        # print(map, key, force_synchronous.get())

        if map[key] == False:
            return
        else:
            map[key]=False

        #  if we have a  discrete action that needs to wait and can't be asynchronous, then we can't use the cron job and as a result we have to do it synchronously on the pedal raise.
        if force_synchronous.get() == True:
            if key == "left":
                print("left up")
                actions.user.left_up( )
            elif key == "right":
                actions.user.right_up( )
            elif key == "center":
                actions.user.center_up( )

    def left_center_right_down():
        """Left, Center and Right pedal"""
        print("Switching mode")
        if "sleep" in scope.get("mode"):
            actions.speech.enable()
        else:
            actions.speech.disable()

    def center_right_down():
        """Center and Right pedal"""
        print("Switching mode")
        if "sleep" in scope.get("mode"):
            actions.speech.enable()
        else:
            actions.speech.disable()

    def left_right_down():
        """Left and Right pedal"""
        ctx.settings['user.pedal_scroll_amount'] = pedal_scroll_amount.get()
        ctx.settings['user.pedal_scroll_amount']+=0.2
        print(ctx.settings['user.pedal_scroll_amount'])

    def left_center_down():
        """Left and Center pedal"""
        print('testing some random stuff here')


    def left_down():
        """Left pedal"""
        actions.user.mouse_scroll_down(pedal_scroll_amount.get())

    def right_down():
        """Right pedal"""
        actions.user.mouse_scroll_up(pedal_scroll_amount.get())
    def center_down():
        """Center pedal"""
        ctx.settings['user.pedal_scroll_amount'] = 0.2


    def left_up():
        """Left pedal up"""
    def right_up():
        """Right pedal up"""
    def center_up():
        """Center pedal up"""