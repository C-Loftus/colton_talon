from ..game.hotspotGenerator.hotspot import getHotSpots, Hotspot
from ..game.automove_actions import APP_NAMES
from typing import assert_never
from talon import ui, actions, cron, settings
from talon.screen import Screen
from enum import Enum
import time

# The quadrants are defined on a monitor as follows:
# # +------------+
# # |\          /|
# # | \        / |
# # |  \  up  /  |
# # |   \    /   |
# # |left+--right|
# # |   /   \    |
# # |  /     \   |
# # | / down  \  |
# # |/         \ |
# # +------------+

tracker_job = None
CRON_INTERVAL = "500ms"
ScreenQuadrant = Enum('screenQuadrant', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
screen: Screen = ui.main_screen()
rect = screen.rect
focusedQuadrant: type[ScreenQuadrant]

def on_app_switch(application):
    global tracker_job
    if application.name == "Visual Studio Code":
        cron.cancel(tracker_job)
        return

    if application.name in APP_NAMES or settings.get("user.automove_debug"):
        print(f'Starting cron interval at {CRON_INTERVAL}')
        tracker_job = cron.interval(CRON_INTERVAL, handleCursor)
    else:
        cron.cancel(tracker_job)
    
# when there is a change in the active app, check if it is one of the apps we want 
ui.register("app_activate", on_app_switch)

def isAboveNegativeSlope() -> bool:
    """check if in quadrants UP or RIGHT 
    (ie if the mouse is above the line y = x))
    """
    slope = rect.height / rect.width
    line_y = slope * actions.mouse_x()
    
    return True if actions.mouse_y() < line_y else False


def isAbovePositiveSlope() -> bool:
    """check if in quadrants UP or LEFT
    (ie if the mouse is above the line y = -x)
    """

    slope = rect.height / rect.width
    line_y = slope * (rect.width - actions.mouse_x())
    
    return True if actions.mouse_y() < line_y else False


def handleCursor():

    hotSpots = getHotSpots()

    for hotSpot in hotSpots: 
        if hotSpot.cursorInside() and settings.get("user.hotspot_show"):
            match hotSpot.get_unique_id():
                case 1:
                    actions.user.hotspot_1_focus()  
                case 2:
                    actions.user.hotspot_2_focus()
                case 3:
                    actions.user.hotspot_3_focus()
                case 4:
                    actions.user.hotspot_4_focus()
                case _:
                    assert_never()
    
    
    global focusedQuadrant

    match (isAboveNegativeSlope(), isAbovePositiveSlope()):
        case True, True:
            focusedQuadrant = ScreenQuadrant.UP
        case True, False:
            focusedQuadrant = ScreenQuadrant.RIGHT
        case False, False:
            focusedQuadrant = ScreenQuadrant.DOWN
        case False, True:
            focusedQuadrant = ScreenQuadrant.LEFT
        case _:
            assert_never()

    if settings.get("user.automove_debug") and int(time.time()) % 5 == 0:
        print(f'{actions.mouse_y()=},{actions.mouse_x()=}')
        print(f'{focusedQuadrant=}')

    #  don't call an action unless it has been hovered for a  significant threshold

    hotspots: list[Hotspot] = getHotSpots()
    cursorInHotspot = any([hotspot.cursorInside() for hotspot in hotspots])
    #  don't call an action unless it has been hovered for a  signif andicant threshold
    if sufficient_threshold(focusedQuadrant) and not cursorInHotspot and settings.get("user.automove_enabled"): 
        match focusedQuadrant:
            case ScreenQuadrant.UP: 
                actions.user.on_quadrant_up_focus()
            case ScreenQuadrant.RIGHT: 
                actions.user.on_quadrant_right_focus()
            case ScreenQuadrant.DOWN: 
                actions.user.on_quadrant_down_focus()
            case ScreenQuadrant.LEFT: 
                actions.user.on_quadrant_left_focus()

stare_map = {
    ScreenQuadrant.UP : 0,
    ScreenQuadrant.RIGHT:0,
    ScreenQuadrant.DOWN:0,
    ScreenQuadrant.LEFT:0
}

def sufficient_threshold(focusedQuadrant) -> bool:
    
    # remove the "ms" unit from the cron interval
    to_int = lambda cron_fmt: int(cron_fmt[:-2])
  
    stare_map[focusedQuadrant]+= to_int(CRON_INTERVAL)

    for quadrant in stare_map:
        if quadrant != focusedQuadrant:
            stare_map[quadrant]=0

    if stare_map[focusedQuadrant] >= to_int(settings.get("user.automove_trigger_threshold")):
        return True
    else:
        return False



