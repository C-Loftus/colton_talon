from talon import Context, Module, actions, settings

ctx = Context()
ctx.matches = """app: vscode
and title: /ipynb/
not title: /Interactive/
not tag: user.controlTabsWithPedal
"""

ctx.settings["user.oneActionPerPedalPress"] = True

pedal_scroll_amount = settings.get("user.pedal_scroll_amount")
scroll, jump = False, False

@ctx.action_class("user")
class Actions:

    def west_down():
        if not settings.get("user.oneActionPerPedalPress") and scroll:
            actions.user.mouse_scroll_down(pedal_scroll_amount)

    def east_down():
        if not settings.get("user.oneActionPerPedalPress") and scroll:
            actions.user.mouse_scroll_up(pedal_scroll_amount)

    def east_west_down():
        global scroll
        scroll = not scroll
        print("Switching scroll mode to", scroll)
        ctx.settings["user.oneActionPerPedalPress"] = not ctx.settings["user.oneActionPerPedalPress"]
        if scroll:
            print("Scroll amount is", pedal_scroll_amount)
        

    def west_up():
        """Left pedal"""
        actions.user.vscode("jupyter.gotoPrevCellInFile")
        actions.user.vscode("notebook.focusPreviousEditor")
        

    def east_up():
        """Right pedal"""
        if not jump:
            actions.user.vscode("jupyter.runcurrentcell"); 
            actions.user.vscode("notebook.cell.execute")
        actions.user.vscode("jupyter.gotoNextCellInFile")
        actions.user.vscode("notebook.focusNextEditor")

    def north_up():
        """Center pedal"""

        actions.user.vscode("jupyter.runcurrentcell"); 
        actions.user.vscode("notebook.cell.execute")

