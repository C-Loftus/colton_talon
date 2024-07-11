os: mac

-

# for some reason on mac the timeout is different
settings():
    user.subtitles_timeout_per_char = 20
    # 750ms is the minimum timeout for a subtitle
    user.subtitles_timeout_min = 75
    # 3 seconds is the maximum timeout for a subtitle
    user.subtitles_timeout_max = 120
    # Subtitles are positioned at the bottom of the screen
    user.subtitles_y = 0.93
