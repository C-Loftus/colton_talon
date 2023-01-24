# activate this .talon file if the current app name is "Chrome"
# you can find app names by running ui.apps() in the REPL
app.name: Google-chrome
-
# key_wait increases the delay when pressing keys (milliseconds)
# this is useful if an app seems to jumble or drop keys
# settings():
#     key_wait = 4.0

# activate the global tag "browser"
tag(): browser

# define some voice commands

switch tab: key(ctrl-tab)

listen:
    key(ctrl-shift-s)
    speech.disable()
  
    
close tab:
    key(ctrl-w)