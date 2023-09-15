mode: command
tag: user.python
-

talon boilerplate:
    
    user.paste("""from talon import Module, actions\n\nmod = Module()\n\n@mod.action_class\nclass Actions:\n    def ():""")
    user.paste("\n     ''''''\n")
    key(up:2)
    key(right:8)

new format string:
    user.paste("f'{ }'")
    key(left:3)    
   