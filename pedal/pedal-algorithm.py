from talon import Module, actions, cron, scope, Context, settings
import time
from typing import TypedDict
from .pedal_types import PedalStateMap

mod = Module()
ctx = Context()

map = PedalStateMap(bool)
held_seconds = PedalStateMap(float)
# Trigger a hold if a key has been held for SEC_TO_TRIGGER seconds
# check if this threshold is met every SEC_TO_CHECK seconds
SEC_TO_TRIGGER = 2


def on_interval() -> None:

    # if map contains at least 2 true values, then we have a double keypress
    if map.multiple_held():

        if map["left"] and map["right"]:
            
            actions.user.left_right_down()
        elif map["left"] and map["center"]:
            actions.user.left_center_down()
        elif map["center"] and map["right"]:
            actions.user.center_right_down()
    
        map.reset()
        return  

    # with synchronous code we only call functions on the pedal up
    # pedal down functions  can be asynchronous and held down to repeat,
    #  which is impossible if we have to force synchronous
    if settings.get("user.oneActionPerPedalPress"):
        return

    if map["center"] and not settings.get("user.oneActionPerPedalPress"):
        actions.user.center_down()
    elif map["left"]:
        actions.user.left_down()
    elif map["right"]:
        actions.user.right_down()



@mod.action_class
class Actions:

    def pedal_down(key: str):
        """Map the key name to down"""
        map[key]=True


    def pedal_up(key: str):
        """Pedal up"""
        # If you have a synchronous double keypress that has already reset the map, then we don't want to do anything.
        # this prevents single actions mistakenly firing after the double action
        if map[key] == False or held_seconds.wasHeld == True:
            held_seconds.wasHeld = False
            return
        else: 
            map[key]=False


        # if we have a  discrete action that needs to block (wait for return) and can't be asynchronous, 
        # then we can't use the cron job for quick calls in succession and as a result we have to do 
        # it synchronously on the pedal raise to only call it once
        if settings.get("user.oneActionPerPedalPress") == True:
            match key:
                case "left":
                    actions.user.left_up( )
                case "right":
                    actions.user.right_up( )
                case "center":
                    actions.user.center_up()

        elif settings.get("user.oneActionOnCenterPress") == True and key == "center":
            actions.user.center_up()



def pedal_held_down() -> None:

    for pedalDirection in map:
        isHeldDown = map[pedalDirection]
        if isHeldDown == True:
            held_seconds[pedalDirection] += CHECK_INTERVAL
        else:
            held_seconds[pedalDirection] = 0
    
        if held_seconds[pedalDirection] == SEC_TO_TRIGGER:
            # We reset the hold time so we can potentially trigger the action again after the trigger time passes once more.
            
            held_seconds.reset()

            # we only want to trigger on synchronous actions since if it was asynchronous We might trigger it by mistake, 
            # for instance if you were scrolling down a lot and end up holding the pedal for 5 seconds

            if settings.get("user.oneActionOnCenterPress") and pedalDirection == "center":
                actions.user.held_center()
                
            elif settings.get("user.oneActionPerPedalPress"):
                print(f'{pedalDirection} hold triggered')

                match pedalDirection:
                    case "right":
                        actions.user.held_right()
                    case "center":
                        actions.user.held_center()
                    case "left":
                        actions.user.held_left()
            else: 
                return
            
            # we need to reset the map so we don't call the up function
            # as well on release of the pedal
            held_seconds.reset()
            held_seconds.wasHeld = True

cron.interval("16ms", on_interval)
cron.interval(cron.seconds_to_timespec(CHECK_INTERVAL := .5), pedal_held_down)
