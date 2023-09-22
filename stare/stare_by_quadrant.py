from .stare_actions import APP_NAMES
from typing import assert_never
from talon import ui, actions, cron, settings
from talon.screen import Screen
from enum import Enum

ScreenQuadrant = Enum('screenQuadrant', ['UP', 'DOWN', 'LEFT', 'RIGHT'])
screen: Screen = ui.main_screen()
rect = screen.rect
focusedQuadrant: type[ScreenQuadrant]

def runQuadrantAction(focusedQuadrant):
    match focusedQuadrant:
        case ScreenQuadrant.UP: 
            actions.user.on_quadrant_up_focus()
        case ScreenQuadrant.RIGHT: 
            actions.user.on_quadrant_right_focus()
        case ScreenQuadrant.DOWN: 
            actions.user.on_quadrant_down_focus()
        case ScreenQuadrant.LEFT: 
            actions.user.on_quadrant_left_focus()

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


def getQuadrant():
    """get the quadrant the mouse is in"""
    
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

    return focusedQuadrant