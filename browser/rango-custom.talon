tag: browser
and tag: user.rango_direct_clicking
title: /File Browser/
-

settings():
    # Enable if you'd like the picker gui to automatically appear when explorer has focus
    user.file_manager_auto_show_pickers = 0

^<user.rango_target>$: 
    user.rango_command_with_target("directClickElement", rango_target)
    user.rango_command_with_target("clickElement", rango_target)
