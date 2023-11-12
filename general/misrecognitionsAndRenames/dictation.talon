mode: dictation
not app: vscode

-
folk is code:               user.focus_vscode()
folk is chrome:             user.focus_chrome()

#Match cursorless syntax
format <user.formatters> at this: user.formatters_reformat_selection(formatters)

question work:              "?"

^left$:
    key(ctrl-backspace)

^iter$:
    key(enter)

^tell the close$:           user.tab_close_wrapper()
