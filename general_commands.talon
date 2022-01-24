mode: command

-
start timer:
    # work time, break time
    user.start_timer(20, 5)

custom timer <digits> <digits>:
    user.start_timer("{digits_1}", "{digits_2}")

stop timer:
    user.stop_timer()

reset window tiling:
    key(super-r)
    sleep(.25)
    key(super-e)
    print("reset window tiling")

copy <digits> lines:
    edit.extend_line_end() 
    edit.extend_line_down() 
    repeat(digits-2)
    edit.copy()
    
smile:
    user.paste("(* ^ ω ^)")

go left <digits>:
    key("left:{digits_1}")
go right <digits>:
    key("right:{digits_1}")
go down <digits>:
    key("down:{digits_1}")
go up <digits>:
    key("up:{digits_1}")