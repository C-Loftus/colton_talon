mode: command
-

^erase note <digits>$:
     user.erase_note("{digits_1}")
^pencil note <user.text>$:
     user.pencil_note(text)
toggle notes:  
     user.toggle_notes()
^backup notes$:
     user.backup_notes()
^log notes$:
     user.log_notes()
^trash notes$:
     user.backup_notes()
     user.trash_notes()
^erase page <user.text>$:
     user.erase_page(text)
^new page <user.text>$:
     user.new_page(text)
switch page <user.text>:
     user.switch_page(text)

