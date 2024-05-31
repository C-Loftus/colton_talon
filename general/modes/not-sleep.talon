not mode: sleep

-

^mixed mode$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
^blender$:
    mode.disable("sleep")
    mode.enable("dictation")
    mode.enable("command")
