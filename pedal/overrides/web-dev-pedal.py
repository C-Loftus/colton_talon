import time

from talon import Context, Module, actions

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


ctx.settings["user.oneActionPerPedalPress"] = False


@ctx.action_class("user")
class Actions:

    # def east_west_down():
    #     """Left and Right pedal"""

    # def west_up():
    #     """left pedal"""

    # def west_down():
    #     """left pedal down"""

    # defnorth_down():

    def north_up():
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

    # def east_down():
    #     """right pedal down"""

    # def north_up():
    #     """center pedal"""
