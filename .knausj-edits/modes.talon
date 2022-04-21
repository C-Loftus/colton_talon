not mode: sleep
-
^dictation mode$:
    mode.disable("sleep")
    mode.disable("command")
    mode.enable("dictation")
    user.code_clear_language_mode()
    mode.disable("user.gdb")
    user.draw_mode("dictation")

^command mode$:
    mode.disable("sleep")
    mode.disable("dictation")
    mode.enable("command")
    user.draw_mode("command")


^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
    user.draw_mode("mixed")


^blender$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
    user.draw_mode("mixed")