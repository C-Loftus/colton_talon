from talon import Context, actions

ctx = Context()
ctx.matches = "app: vscode"

@ctx.action_class("user")
class CodeActions:
    
    def left_pedal():
        pass
    def right_pedal():
        pass
    def center_pedal():
        pass

    def left_pedal_up():
        actions.user.vscode("jupyter.gotoPrevCellInFile")
    def right_pedal_up():
        actions.user.vscode("jupyter.gotoNextCellInFile")
    def center_pedal_up():
        actions.user.vscode("jupyter.runcurrentcell")




    
    