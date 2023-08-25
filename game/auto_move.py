from typing import assert_never
from talon import Module, Context, app, registry, scope, skia, ui, actions, cron
from talon.canvas import Canvas
from talon.screen import Screen
from talon.skia.canvas import Canvas as SkiaCanvas
from talon.skia.imagefilter import ImageFilter
from talon.types import Rect
from enum import Enum
from dataclasses import dataclass

# +------------+
# |\          /|
# | \        / |
# |  \  up  /  |
# |   \    /   |
# |left+--right|
# |   /   \    |
# |  /     \   |
# | / down  \  |
# |/         \ |
# +------------+

mod = Module()
ctx = Context()
ctx.matches = r"""
title: /ynoproject.net/
"""
horizontal_position = mod.setting(
    "my_user_file_set_horizontal_position",
    type=int,
    default=0,
    desc="Set the horizontal display position of some UI element",
)

CRON_INTERVAL = "100ms"
TRIGGER_THRESHOLD = "2000ms"
ScreenQuadrant = Enum('screenQuadrant', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
screen: Screen = ui.main_screen()
rect = screen.rect
focusedQuadrant: type[ScreenQuadrant]


DEBUG = False

def isAboveNegativeSlope() -> bool:
    """check if in quadrants UP or RIGHT"""
    # 1080 / 1920 = .5625 
    slope = rect.height / rect.width
    line_y = slope * actions.mouse_x()

    if DEBUG:
        print(f'{actions.mouse_y()=}, {line_y=}, {actions.mouse_x()=}')

    if actions.mouse_y() < line_y:
        return True
    else:
        return False


def isAbovePositiveSlope() -> bool:
    """check if in quadrants UP or RIGHT"""

    slope = rect.height / rect.width
    line_y = slope * (rect.width - actions.mouse_x())
    
    if DEBUG:
        print(f'{actions.mouse_y()=}, {line_y=}')

    if actions.mouse_y() < line_y:
        return True
    else:
        return False


def onFocus():
    
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

    if DEBUG:
        print(focusedQuadrant)

    #  don't call an action unless it has been hovered for a  significant threshold
    if sufficient_threshold(focusedQuadrant):
        match focusedQuadrant:
            case ScreenQuadrant.UP: 
                actions.user.on_quadrant_up_focus()
            case ScreenQuadrant.RIGHT: 
                actions.user.on_quadrant_right_focus()
            case ScreenQuadrant.DOWN: 
                actions.user.on_quadrant_down_focus()
            case ScreenQuadrant.LEFT: 
                actions.user.on_quadrant_left_focus()

nop = lambda *a, **k: print("Test")

@ctx.action_class
class Actions:

    def on_quadrant_left_focus():
        """Runs when the left quadrant is focused """
        nop()
    def on_quadrant_right_focus():
        """Runs when the right quadrant is focused """
        nop()
    def on_quadrant_up_focus():
        """Runs when the up quadrant is focused """
        nop()
    def on_quadrant_down_focus():
        """Runs when the down quadrant is focused """
        nop()

print(f'Starting cron interval at {CRON_INTERVAL}')
cron.interval(CRON_INTERVAL, onFocus)


stare_map = {
    ScreenQuadrant.UP : 0,
    ScreenQuadrant.RIGHT:0,
    ScreenQuadrant.DOWN:0,
    ScreenQuadrant.LEFT:0
}

to_int = lambda cron_fmt: int(cron_fmt[:-2])

def sufficient_threshold(stare_location):
    global focusedQuadrant
    if DEBUG:
        print(focusedQuadrant, stare_map)
    stare_map[focusedQuadrant]+= to_int(CRON_INTERVAL)

    for quadrant in stare_map:
        if quadrant != focusedQuadrant:
            stare_map[quadrant]=0

    if stare_map[focusedQuadrant] >= to_int(TRIGGER_THRESHOLD):
        return True
    else:
        return False





