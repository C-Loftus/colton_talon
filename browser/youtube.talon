title: /YouTube/
title: /Invidious/

-
# settings():
#     key_wait = 10.0

jump left: 
    key(ctrl-left)
jump right: 
    key(ctrl-right)
speed up <digits>:
    key("d:{digits_1}")
speed down <digits>:    
    key("s:{digits_1}")

ten: ""

search <user.text>:
    key("/")
    key(ctrl-a)
    "{user.text}"
    key(enter)

next chapter: 
    key(ctrl-right)

previous chapter: 
    key(ctrl-left)


toggle mini: 
    key(i)