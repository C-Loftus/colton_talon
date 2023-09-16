from ..game.hotspotGenerator.hotspot import getHotSpots, Hotspot
from ..game.automove_actions import APP_NAMES
from typing import assert_never
from talon import Module, Context, app, registry, scope, skia, ui, actions, cron, settings
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
CRON_INTERVAL = "100ms"
ScreenQuadrant = Enum('screenQuadrant', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
screen: Screen = ui.main_screen()
rect = screen.rect
focusedQuadrant: type[ScreenQuadrant]

def on_app_switch(application):
    global tracker_job
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

    if sufficient_threshold(focusedQuadrant) and not cursorInHotspot(hotspots):
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

# remove the "ms" unit from the cron interval
to_int = lambda cron_fmt: int(cron_fmt[:-2])

def sufficient_threshold(focusedQuadrant) -> bool:
    if settings.get("user.automove_debug"):
        print(focusedQuadrant, stare_map)

    stare_map[focusedQuadrant]+= to_int(CRON_INTERVAL)

    for quadrant in stare_map:
        if quadrant != focusedQuadrant:
            stare_map[quadrant]=0

    if stare_map[focusedQuadrant] >= to_int(settings.get("user.automove_trigger_threshold")):
        return True
    else:
        return False

## TODO fix this
def cursorInHotspot(hotspots: list[Hotspot]) -> bool:
    cursor_y = actions.mouse_y()
    cursor_x = actions.mouse_x()

    # check if the cursor is in any of the hotspots. each hotspot has a x and y coordinate as well as a radius. they are all circles
    for hotspot in hotspots:
        INSIDE_X = hotspot.x - hotspot.radius <= cursor_x <= hotspot.x + hotspot.radius
        INSIDE_Y = hotspot.y - hotspot.radius <= cursor_y <= hotspot.y + hotspot.radius
        if INSIDE_X and INSIDE_Y:
            return True
    return False

