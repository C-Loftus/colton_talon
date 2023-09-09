# This file contains the actions that are called when the cursor 
# is in a quadrant for a certain amount of time. It doesn't handle any 
# of the logic for determining which quadrant the cursor is in. That is
# handled in ../game/auto_move.py

from talon import Module, Context, app, registry, scope, skia, ui, actions, cron, settings
APP_NAMES = ["ynoproject.net"]

mod = Module()
ctx = Context()
ctx.matches = f"""
title: /{APP_NAMES[0]}/
"""

@mod.action_class
class Actions:

    def on_quadrant_left_focus():
        """Runs when the left quadrant is focused """
        actions.key("left")
    def on_quadrant_right_focus():
        """Runs when the right quadrant is focused """
        actions.key("right")
    def on_quadrant_up_focus():
        """Runs when the up quadrant is focused """
        actions.key("up")
    def on_quadrant_down_focus():
        """Runs when the down quadrant is focused """
        actions.down("down")

    def hotspot_1_focus():
        """Runs when the first hotspot is focused """

    def hotspot_2_focus():
        """Runs when the second hotspot is focused """

    def hotspot_3_focus():
        """Runs when the third hotspot is focused """

    def hotspot_4_focus():
        """Runs when the fourth hotspot is focused """

mod.setting(
    "automove_trigger_threshold",
    type=str,
    default="2000ms",
    desc="How long the cursor needs to be in one quadrant before the action is called",
)

mod.setting(
    "automove_debug",
    type=bool,
    default=False,
    desc="Whether to print debug statements",
)

