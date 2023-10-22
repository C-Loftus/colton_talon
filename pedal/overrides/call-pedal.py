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
app: /zoom meetings/i
"""

zoom_context = Context()
zoom_context.matches = """
app: /zoom meetings/i
"""

teams_context = Context()
teams_context.matches = """
app: /microsoft teams/i
app: teamsCallInBrowser
"""


ctx.settings["user.oneActionPerPedalPress"] = True

@ctx.action_class("user")
class CallActions:

    def west_up():
        # os.system("amixer -D pulse sset Master 5%- > /dev/null")
        actions.key("voldown")

    def east_up():
        actions.key("volup")

@teams_context.action_class("user")
class TeamsActions:

    def east_west_down():
        actions.key("ctrl-shift-m")

@zoom_context.action_class("user")
class ZoomActions:

    def east_west_down():
        actions.key("alt-a")