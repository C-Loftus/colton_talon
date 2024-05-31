mode: all
-

^[<phrase>] drowsy$:
    speech.disable()
^one (sec | second)$:
    speech.disable()
^(hey | he) (siri | serie)$:
    speech.disable()
^trouser$:
    speech.disable()

^(stop listening)+$:
    speech.enable()

^(start listening)+$:
    speech.disable()
