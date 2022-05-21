mode: command
-

erase note <digits>:
     user.erase_note("{digits_1}")
^pencil note <phrase>$:
     user.pencil_note(phrase)
toggle notes:
     user.toggle_notes()
export my notes:
     user.export_notes()
trash notes:
     user.trash_notes()

trash page <user.text>:
     user.trash_page(text)

new page <user.text>:
     user.new_page(text)

switch page <user.text>$:
     user.switch_page(text)

