from talon import Module, actions, cron, settings
from .pedal_types import PedalStateMap

mod = Module()

map = PedalStateMap(bool)
held_seconds = PedalStateMap(float)


def handle_down_pedal() -> None:

    # Double presses are always triggered and thus don't need to be checked for
    if map.multiple_held():

        match sorted(map.held_pedals()):
            case ["left", "right"]:
                actions.user.left_right_down()
            case ["center", "right"]:
                actions.user.center_right_down()
            case ["center", "left"]:
                actions.user.left_center_down()
            case ["center", "left", "right"]:
                actions.user.left_center_right_down()
    
        map.reset()
        return  

    # Only trigger the up action once if the setting is enabled
    # So we should return and skip the down action if the setting is enabled
    if settings.get("user.oneActionPerPedalPress"):
        return

    if map["center"] and not settings.get("user.oneActionOnCenterPress"):
        actions.user.center_down()
    elif map["left"]:
        actions.user.left_down()
    elif map["right"]:
        actions.user.right_down()



@mod.action_class
class Actions:

    def pedal_down(key: str):
        """Map the key name to down"""

        if key not in map.pedals:
            raise KeyError(f'Pedal must be in {map.pedals }')

        map[key]=True


    def pedal_up(key: str):
        """Pedal up"""

        if key not in map.pedals:
            raise KeyError(f'Pedal must be in {map.pedals }')

        # If you have a double keypress that has already reset the map, then 
        # we don't want to do anything.
        # This prevents single actions mistakenly firing after the double action
        if map[key] == False or held_seconds.wasHeld == True:
            held_seconds.wasHeld = False
            # If it was held we don't want to call the up function as well
            return
        else: 
            map[key]=False


        # If we are doing more than one action on a pedal press
        # then we don't want to call the up function as well
        if settings.get("user.oneActionPerPedalPress") == False:
            
            if settings.get("user.oneActionOnCenterPress") == True and key == "center":
                actions.user.center_up()
            return

        match key:
            case "left":
                actions.user.left_up( )
            case "right":
                actions.user.right_up( )
            case "center":
                actions.user.center_up()


def handle_held_pedal() -> None:

    for pedalDirection in map:
        isPressed = (map[pedalDirection] == True)
        if isPressed:
            held_seconds[pedalDirection] += CHECK_INTERVAL
        else:
            held_seconds[pedalDirection] = 0

        if held_seconds[pedalDirection] == settings.get("user.secondsToTriggerPedalHold"):

            # only trigger on oneAction pedals since we don't want a repeated call to also 
            # trigger a hold (ie scrolling down should not also trigger a hold)
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

            # if no hold was triggered, just return
            # and don't do anything with the map
            else: 
                return
            
            # we need to reset the map so we don't call the up function
            # as well on release of the pedal
            held_seconds.reset()
            held_seconds.wasHeld = True

cron.interval("16ms", handle_down_pedal)
cron.interval(cron.seconds_to_timespec(CHECK_INTERVAL := .5), handle_held_pedal)
