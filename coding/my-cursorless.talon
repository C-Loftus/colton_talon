mode: command
mode: user.cursorless_spoken_form_test
tag: user.cursorless
-

merge <user.cursorless_target>:
    user.cursorless_command("setSelection", cursorless_target)
    user.paste(user.remove_spaces(edit.selected_text()))
