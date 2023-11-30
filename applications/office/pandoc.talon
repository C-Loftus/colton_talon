title: /.md/
title: /.txt/
app: vscode

-


compile {user.pandoc_output_format}: 
    path = user.get_dirname()
    user.vscode("workbench.action.terminal.focus")
    clip.set_text("mkdir -p 2>$null '{path}/build'; cd '{path}'; ")
    key(ctrl-shift-v)

    file = user.get_basename()
    user.compile_with_pandoc(file, user.pandoc_output_format)
    sleep(0.2)
    key(enter)

open compiled {user.pandoc_output_format}:
    user.vscode("workbench.action.terminal.focus")
    file = user.get_full_path()
    user.open_compiled_file(file, user.pandoc_output_format)


check compiled {user.pandoc_output_format} [<number_small>]:
    user.vscode("workbench.action.terminal.focus")

    file = user.get_full_path()
    number_small = number_small or 10
    user.check_compiled_file(file, user.pandoc_output_format, number_small)

compile and check {user.pandoc_output_format} [<number_small>]:
    path = user.get_dirname()
    user.vscode("workbench.action.terminal.focus")
    clip.set_text("mkdir -p  2>$null '{path}/build'; cd '{path}'; ")
    key(ctrl-shift-v)

    file = user.get_basename()
    user.compile_with_pandoc(file, user.pandoc_output_format)
    sleep(0.2)
    key(enter)

    file = user.get_full_path()
    number_small = number_small or 10
    user.check_compiled_file(file, user.pandoc_output_format, number_small)