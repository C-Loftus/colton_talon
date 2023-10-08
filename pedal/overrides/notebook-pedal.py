from talon import Context, Module, actions, settings
import time, multiprocessing

ctx = Context()
ctx.matches = """app: vscode
and title: /ipynb/
"""

ctx.settings["user.oneActionPerPedalPress"] = True

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
scroll, jump = False, False

@ctx.action_class("user")
class Actions:

    def left_down():
        if not settings.get("user.oneActionPerPedalPress") and scroll:
            actions.user.mouse_scroll_down(pedal_scroll_amount)

    def right_down():
        if not settings.get("user.oneActionPerPedalPress") and scroll:
            actions.user.mouse_scroll_up(pedal_scroll_amount)

    def left_right_down():
        global scroll
        scroll = not scroll
        print("Switching scroll mode to", scroll)
        ctx.settings["user.oneActionPerPedalPress"] = not ctx.settings["user.oneActionPerPedalPress"]
        if scroll:
            print("Scroll amount is", pedal_scroll_amount)
        

    def left_up():
        """Left pedal"""
        actions.user.vscode("jupyter.gotoPrevCellInFile")
        actions.user.vscode("notebook.focusPreviousEditor")
        

    def right_up():
        """Right pedal"""
        if not jump:
            actions.user.vscode("jupyter.runcurrentcell"); 
            actions.user.vscode("notebook.cell.execute")
        actions.user.vscode("jupyter.gotoNextCellInFile")
        actions.user.vscode("notebook.focusNextEditor")

    def center_up():
        """Center pedal"""

        actions.user.vscode("jupyter.runcurrentcell"); 
        actions.user.vscode("notebook.cell.execute")

