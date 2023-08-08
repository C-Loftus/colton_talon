title: /.rmd/

-

tag(): user.r

code block:
    '\n```'
    user.paste("{}")
    key(left)
    "r"
    key(end)
    "\n\n```"
    key(up)

run line:
    key(ctrl-enter)

run chunk: 
    user.vscode("r.runCurrentChunks")

run all:
    user.vscode("r.runAllChunks")

run above:
    user.vscode("r.runAboveChunks")

run below:
    user.vscode("r.runBelowChunks")