from talon import Context, Module, actions

ctx = Context()
mod = Module()

mod.apps.teamsCallInBrowser = r"""
    title: /modern-calling/
    tag: browser
"""
ctx.matches = """
app: teamsCallInBrowser
app: /microsoft teams/i
"""

speed_mode = False

ctx.settings["user.force_synchronous"] = True

@ctx.action_class("user")
class Actions:

    def left_up():
        # os.system("amixer -D pulse sset Master 5%- > /dev/null")
        actions.key("voldown")

    def right_up():
        actions.key("volup")

    def left_right_down():
        actions.key("ctrl-shift-m")
        
