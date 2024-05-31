tag: user.fluentSearchHintsOpen
-

^<user.letter> <user.letter>$:
    key(letter)
    key(letter_2)
    sleep(.5)
    key(ctrl-alt-;)

^fluent search$:
    user.toggleFluentSearchTags()

# key(escape):
#     key(escape)
#     user.toggleFluentSearchTags()
