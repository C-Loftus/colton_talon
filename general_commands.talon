mode: command

-

copy <digits> lines:
    edit.extend_line_end() 
    edit.extend_line_down() 
    repeat(digits-2)
    edit.copy()
    
smile:
    user.paste("(* ^ ω ^)")