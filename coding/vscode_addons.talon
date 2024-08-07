app: vscode
mode: command
not mode: dictation
-

# used for cursorless chaining
then:
    skip()

hats permanently off:
    user.change_setting("cursorless.showOnStart", "false")

hats permanently on:
    user.change_setting("cursorless.showOnStart", "true")

new window:
    key(ctrl-shift-n)

focus lines:
    key(ctrl-1)

run last:
    user.vscode("workbench.action.terminal.focus")
    key(up)
    key(enter)
    
kill program:
    user.vscode("workbench.action.terminal.focus")
    sleep(.25)
    key(ctrl-c)

hints toggle:
    user.vscode("cursorless.toggleDecorations")

restart python:
    key(ctrl-shift-alt-f)
    sleep(.25)
    key(ctrl-c)
    key(ctrl-s)
    sleep(.1)
    key(ctrl-shift-alt-d)
    sleep(.1)
    key(ctrl-f10)

run again:
    user.vscode("workbench.action.terminal.focus")
    sleep(.25)
    key(up)
    sleep(.25)
    key(enter)

backup:
    key(ctrl-shift-alt-f)
    user.paste("fgc")
    key(enter)

switch project:
    key(ctrl-r)
    sleep(0.25)
    key(enter)

special:
    "``"
    key(left:1)

close folders:
    user.vscode("workbench.files.action.collapseExplorerFolders")
# bar collapse: user.vscode("workbench.files.action.collapseExplorerFolders")

format document:
    user.vscode("editor.action.formatDocument")

run rust:
    user.vscode("workbench.action.terminal.focus")
    sleep(.1)
    "cargo run"
    sleep(.1)
    key(enter)
    
run typescript:
    user.vscode("workbench.action.terminal.focus")
    sleep(.3)
    user.paste("npx ts-node src/")

dance:
    "// "
run that:
    key(ctrl-shift-enter)

^question work$:
    "?"

bar activity:
    user.vscode("workbench.action.toggleActivityBarVisibility")

toggle terminal:
    user.vscode("workbench.action.terminal.toggleTerminal")

pull user directory:
    user.vscode("workbench.action.terminal.focus")
    sleep(.1)
    user.paste("bash -c 'find . -name .git -print -execdir git pull \\;")
    sleep(.1)
    key(enter)

enable completions:
    user.change_setting("github.copilot.editor.enableAutoCompletions", true)

disable completions:
    user.change_setting("github.copilot.editor.enableAutoCompletions", false)
