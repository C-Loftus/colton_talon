mode: command
-

note scratch <user.text>:
    user.append_to_note(text)

note copy:
    user.copy_note()

^note delete$:
    user.clear_note()

^note copy backup$:
    user.copy_backup_note()
