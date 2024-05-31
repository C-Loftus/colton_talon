tag: user.asArduino
app: vscode

-

gamepad(east):
    user.vscode("workbench.action.toggleZenMode")
gamepad(west):
    key(tab)
gamepad(south):
    key(enter)
gamepad(north:down):
    user.pedal_down("south")

gamepad(north:up):
    user.pedal_up("south")
