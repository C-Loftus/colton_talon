os: windows
app: vscode
-

update talon scripts:
    user.vscode("workbench.action.terminal.focus")
    build_path = user.relative_dir_to_talon_home("colton_talon^update")
    clip.set_text("cd '{build_path}'; ./update.ps1")
    key(ctrl-shift-v)
    key(enter)
