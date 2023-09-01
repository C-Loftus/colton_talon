mode: command
tag: user.python
-

python boilerplate:
    
    user.paste("""from talon import Module, actions\n\nmod = Module()\n\n@mod.action_class\nclass Actions:\n\tdef ():""")
    # user.paste("""\n''' '''\n """)
    user.paste("\n\t''''''\n")
    key(up:2)
    key(right:5)

    
   