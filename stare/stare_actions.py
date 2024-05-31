# This file contains the actions that are called when the cursor
# is in a quadrant for a certain amount of time. It doesn't handle any
# of the logic for determining which quadrant the cursor is in. That is
# handled in ../game/auto_move.py

from talon import Module, actions

APP_NAMES = ["ynoproject.net"]

mod = Module()


@mod.action_class
class Actions:

    def on_quadrant_left_focus():
        """Runs when the left quadrant is focused"""
        actions.key("left")

    def on_quadrant_right_focus():
        """Runs when the right quadrant is focused"""
        actions.key("right")

    def on_quadrant_up_focus():
        """Runs when the up quadrant is focused"""
        actions.key("up")

    def on_quadrant_down_focus():
        """Runs when the down quadrant is focused"""
        actions.key("down")

    def hotspot_1_focus():
        """Runs when the first hotspot is focused"""
        actions.user.notify("test")

    def hotspot_2_focus():
        """Runs when the second hotspot is focused"""
        actions.user.notify("test2")
        print("hotspot focus 2")

    def hotspot_3_focus():
        """Runs when the third hotspot is focused"""
        actions.user.notify("test3")
        print("hotspot focus 3")

    def hotspot_4_focus():
        """Runs when the fourth hotspot is focused"""


mod.setting(
    "thresholdToTriggerStare",
    type=str,
    default="2000ms",
    desc="How long the cursor needs to be in one quadrant before the action is called",
)


mod.setting(
    "stare_debug",
    type=bool,
    default=False,
    desc="Whether to print debug statements",
)

mod.setting(
    "stare_by_quadrant_enabled",
    type=bool,
    default=False,
    desc="Whether to print debug statements",
)
