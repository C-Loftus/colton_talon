os: windows
-

speak this:
    key(ctrl-c)
    text = clip.text()
    user.text_to_speech(text)


# We don't have a guarantee that the item will be correctly orders
#  so we just approximate the location and that the user has to press enter
copy path:
    key(shift-f10)
    key(down:10)