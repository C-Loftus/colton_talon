mode: command
-

go left <digits>:
    key("left:{digits_1}")
go right <digits>:
    key("right:{digits_1}")
go down <digits>:
    key("down:{digits_1}")
go up <digits>:
    key("up:{digits_1}")

copy <digits> lines:
    edit.extend_line_end()
    edit.extend_line_down()
    repeat(digits - 2)
    edit.copy()
