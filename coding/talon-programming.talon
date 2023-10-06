mode: command
app: vscode
-

python base code:
    user.paste("""from talon import Module, actions\n\nmod = Module()\n\n@mod.action_class\nclass Actions:\n    def ():""")
    user.paste("\n     ''''''\n")
    key(up:2)
    key(right:8)

format string:
    user.paste("f''")
    key(left)
    