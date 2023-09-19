tag: user.fluentSearchHintsOpen
mode:  command
-

^<user.letter> <user.letter>$: 
    key(letter)
    key(letter_2)
    sleep(0.2)
    key(ctrl-alt-;)

^fluent search$:  
    user.toggleFluentSearchTags()
    key(ctrl-alt-;)

# key(escape):
#     key(escape)
#     user.toggleFluentSearchTags()