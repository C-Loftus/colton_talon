code.language: markdown
os: windows

-


compile word: 
    path = user.get_dirname()
    user.vscode("workbench.action.terminal.focus")
    clip.set_text("cd '{path}'; ")
    key(ctrl-shift-v)
    user.compile_word(user.get_basename())
    sleep(0.2)
    key(enter)

compile powerpoint:
    path = user.get_dirname()
    user.vscode("workbench.action.terminal.focus")
    clip.set_text("cd '{path}'; ")
    key(ctrl-shift-v)
    user.compile_powerpoint(user.get_basename())
    sleep(0.2)
    key(enter)

open compiled word:
    user.vscode("workbench.action.terminal.focus")
    file = user.get_full_path()
    user.open_compiled_word(file)

opened compiled powerpoint:
    user.vscode("workbench.action.terminal.focus")
    file = user.get_full_path()
    user.open_compiled_powerpoint(file)

