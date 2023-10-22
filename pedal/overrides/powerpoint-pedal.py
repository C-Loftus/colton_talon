from talon import Context, Module, actions, settings
import time

ctx = Context()
ctx.matches = r"""app: powerpointInBrowser
app: /Microsoft PowerPoint/i
"""
# title: /PowerPoint/

mod = Module()
mod.apps.powerpointInBrowser = """
    title: /pptx/
    tag: browser
"""

ctx.settings["user.oneActionPerPedalPress"] = False
ctx.settings["user.oneActionOnCenterPress"] = False




@ctx.action_class("user")
class Actions:
    def west_down():
        """Left pedal"""
        # un focus any edited text
        actions.key("escape:2")
        actions.key("down")
        time.sleep(0.5)

    def east_down():
        """Right pedal"""
        # un focus any edited text
        actions.key("escape:2")
        actions.key("up")
        time.sleep(0.5)

    def north_down():
        """center pedal"""
        actions.key("tab")
        time.sleep(0.5)



        
