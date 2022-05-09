mode: command
-

erase note <digits>:
     user.erase_note("{digits_1}")
^pencil note <phrase>$:
     user.add_note(phrase)
toggle Notes:
     user.toggle_notes()
export notes:
     user.export_notes()
trash notes:
     user.trash_note()
