from talon import Module, actions, cron
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


def on_interval():
    
    if force_synchronous.get() == True:
        if map["left"] and map["right"]:
            actions.user.left_right_down()
            reset_map()
        return

    if map["left"] and map["right"]:
        actions.user.left_right_down()
        reset_map()
    elif map["left"]:
        actions.user.left_down()
    elif map["right"]:
        actions.user.right_down()
    elif map["center"]:
        actions.user.center_down()


reset_map = lambda: map.update({k: False for k in map.keys()})

hold_timeout = 0.2
scroll_amount = 0.2

cron.interval("16ms", on_interval)


@mod.action_class
class Actions:

    def pedal_down(key: str):
        """Pedal down"""
        map[key]=True


    #  if we have a  discreet action that needs to wait and can't be a synchronous, then we can't use the cron job and as a result we have to do it synchronously on the pedal raise.
    def pedal_up(key: str):
        """Pedal up"""
        map[key]=False

        if force_synchronous.get() == True:
            if key == "left":
                actions.user.left_up( )
            elif key == "right":
                actions.user.right_up( )
            elif key == "center":
                actions.user.center_up( )


    def left_right_down():
        """Left and Right pedal"""
        global scroll_amount 
        scroll_amount += 0.4
        print(scroll_amount)

    def left_down():
        """Left pedal"""
        actions.user.mouse_scroll_down(scroll_amount)
    def right_down():
        """Right pedal"""
        actions.user.mouse_scroll_up(scroll_amount)
    def center_down():
        """Center pedal"""
        global scroll_amount
        scroll_amount = 0.2


    def left_up():
        """Left pedal up"""
        pass
    def right_up():
        """Right pedal up"""
        pass
    def center_up():
        """Center pedal up"""
        # actions.user.mouse_scroll_stop()
        pass
