os: windows
mode: command
-

^Windows disable$: speech.disable()
^ windows wake$: speech.enable()
focus <user.running_applications>: user.switcher_focus(running_applications)