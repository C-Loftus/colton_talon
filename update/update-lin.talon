os: linux
app: vscode

-

update talon scripts:
    user.vscode("workbench.action.terminal.focus")
    build_path = user.relative_dir_to_talon_home("my_talon_scripts^update")
    clip.set_text("cd '{build_path}'; chmod +x update.sh; ./update.sh; cd ..")
    key(ctrl-shift-v)
    key(enter)
