from talon import Context, Module, actions, settings
import time, multiprocessing

ctx = Context()
ctx.matches = """app: vscode
and title: /rmd/
"""

ctx.settings["user.force_synchronous"] = True

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
scroll, jump = False, False

@ctx.action_class("user")
class Actions:

    def left_down():
        if not settings.get("user.force_synchronous") and scroll:
            actions.user.mouse_scroll_down(pedal_scroll_amount)

    def right_down():
        if not settings.get("user.force_synchronous") and scroll:
            actions.user.mouse_scroll_up(pedal_scroll_amount)

    def left_right_down():
        global scroll
        scroll = not scroll
        print("Switching scroll mode to", scroll)
        ctx.settings["user.force_synchronous"] = not ctx.settings["user.force_synchronous"]
        if scroll:
            print("Scroll amount is", pedal_scroll_amount)
        

    def left_up():
        """Left pedal"""
        actions.user.vscode("r.goToPreviousChunk")

    def right_up():
        """Right pedal"""
        if not jump:
            actions.user.vscode("r.runCurrentChunk"); 
        actions.user.vscode("r.goToNextChunk")

    def center_up():
        """Center pedal"""

        actions.user.vscode("r.runCurrentChunk"); 

