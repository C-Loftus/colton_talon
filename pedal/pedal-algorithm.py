from talon import Module, actions, cron, settings, Context
from .pedal_types import PedalStateMap

mod = Module()
ctx = Context()
ctx.tags = []

map = PedalStateMap(bool)
held_seconds = PedalStateMap(float)


mod.tag("disablePedal", desc="Tag to disable pedal presses from doing anything")

def handle_down_pedal() -> None:

    # Double presses are always triggered and thus don't need to be checked for
    if map.multiple_held():

        pedals = map.held_pedals()

        if "east" in pedals and "west" in pedals:
            actions.user.east_west_down()
        elif "east" in pedals and "north" in pedals:
            actions.user.east_north_down()
        elif "north" in pedals and "west" in pedals:
            actions.user.north_west_down()
        elif "east" in pedals and "north" in pedals \
            and "west" in pedals:
            actions.user.east_north_west_down()
        # TODO south

        map.reset()
        return  

    # Only trigger the up action once if the setting is enabled
    # So we should return and skip the down action if the setting is enabled
    if settings.get("user.oneActionPerPedalPress"):
        return

    if map["north"] and not settings.get("user.oneActionOnCenterPress"):
        actions.user.north_down()
    elif map["west"]:
        actions.user.west_down()
    elif map["east"]:
        actions.user.east_down()
    elif map["south"]:
        actions.user.south_down()


@mod.action_class
class Actions:

    def disable_pedal_toggle():
        """Toggle the disablePedal tag"""
        if "user.disablePedal" in ctx.tags:
            ctx.tags = []
        else:
            ctx.tags = ["user.disablePedal"]


    def pedal_down(key: str):
        """Map the key name to down"""

        if key not in map.pedals:
            raise KeyError(f'Pedal must be in {map.pedals }')

        if "user.disablePedal" in ctx.tags:
            return

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
            
            if settings.get("user.oneActionOnCenterPress") == True and key == "north":
                actions.user.north_up()
            return

        match key:
            case "west":
                actions.user.west_up( )
            case "east":
                actions.user.east_up( )
            case "north":
                actions.user.north_up()
            case "south":
                actions.user.south_up()


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
            if settings.get("user.oneActionOnCenterPress") and pedalDirection == "north":
                actions.user.north_center()
                
            elif settings.get("user.oneActionPerPedalPress"):
                print(f'{pedalDirection} hold triggered')

                match pedalDirection:
                    case "west":
                        actions.user.held_west( )
                    case "east":
                        actions.user.held_east( )
                    case "north":
                        actions.user.held_north()
                    case "south":
                        actions.user.held_south()

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
