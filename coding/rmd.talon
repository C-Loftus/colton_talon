title: /.rmd/
mode: command

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

boilerplate:
    user.paste("""---\ntitle: "PDF Summary\nauthor: "Colton Loftus"\ndate: "`r format(Sys.time(), '%d %B, %Y')`"\noutput: html_document\n---\n\n```{r setup, include=FALSE""")
    user.paste("""}\nknitr::opts_chunk$set(echo = TRUE, warning = FALSE)\nlibrary(readr)\nlibrary(dplyr)\n```\n\n""")
    '\n```'
    user.paste("{}")
    key(left)
    "r"
    key(end)
    "\n\n```"
    key(up)
