from talon import Context, actions

ctx = Context()
ctx.matches = """app: vscode
"""

def run_cell():
    actions.user.vscode("jupyter.runcurrentcell"); actions.user.vscode("notebook.cell.execute")

def go_up():
    actions.user.vscode("jupyter.gotoPrevCellInFile")
    actions.user.vscode("notebook.focusPreviousEditor")

def go_down():
    actions.user.vscode("jupyter.gotoNextCellInFile")
    actions.user.vscode("notebook.focusNextEditor")


@ctx.action_class("user")
class CodeActions:
    
    def left_pedal():
        pass
    def right_pedal():
        pass
    def center_pedal():
        pass

    def left_pedal_up():
        go_up()

    def right_pedal_up():
        run_cell()
        go_down()
    def center_pedal_up():
        run_cell()


    
    