from talon import Context, Module, actions
import time

mod = Module()

mod.apps.web_dev = r"""
app:vscode
title: /\.html/i
title: /\.css/i
"""

mod.apps.localhost = r"""
tag: browser
title: /127.0.0.1/
title: /0.0.0.0/
"""
# Match either local development in vscode or localhost in the browser
ctx = Context()
ctx.matches = r"""
app:localhost
app: web_dev
"""


ctx.settings["user.force_synchronous"] = False

@ctx.action_class("user")
class Actions:

    # def left_right_down():
    #     """Left and Right pedal"""

    # def left_up():
    #     """left pedal"""

    # def left_down():
    #     """left pedal down"""   

    # def center_down():

    def center_up():
        """
        Switch between chrome and vscode with a
        pedal press if you are doing web dev
        """
        
        if "Chrome" not in actions.win.title():
            chrome = actions.user.get_running_app("Chrome")
            actions.user.switcher_focus_app(chrome)
            actions.key("ctrl-shift-r")
        else:
            actions.user.switcher_focus("Visual Studio Code")
    

    # def right_down():
    #     """right pedal down"""

    # def center_up():
    #     """center pedal"""

        
