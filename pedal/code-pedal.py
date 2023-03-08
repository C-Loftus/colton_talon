from talon import Context, Module, actions
import time, multiprocessing

ctx = Context()
ctx.matches = """app: vscode
"""

ctx.settings["user.force_synchronous"] = True

@ctx.action_class("user")
class Actions:

    def left_right_down():
        """Left and Right pedal"""
        pass

    def left_up():
        """Left pedal"""
        actions.user.vscode("jupyter.gotoPrevCellInFile")
        actions.user.vscode("notebook.focusPreviousEditor")
        


    def right_up():
        """Right pedal"""
        actions.user.vscode("jupyter.gotoNextCellInFile")
        actions.user.vscode("notebook.focusNextEditor")

    def center_up():
        """Center pedal"""
        actions.user.vscode("jupyter.runcurrentcell"); 
        actions.user.vscode("notebook.cell.execute")
