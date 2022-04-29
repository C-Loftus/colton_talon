mode: command

-
launch tokyo:
    # user.switcher_focus("firefox")
    user.system_command_nb("firefox 0.0.0.0:3000")


launch flask:
    user.system_command_nb("firefox http://127.0.0.1:5000/")
    
flask switch:
    key(ctrl-l)
    key(end)

switch maps:
    key(ctrl-l)
    key(end)
    "/maps"
    key(enter)