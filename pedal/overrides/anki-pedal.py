from talon import Context, actions

ctx = Context()
ctx.matches = r"""
os: windows
app.name: anki.exe
os: windows
app.exe: anki.exe
"""

ctx.settings["user.oneActionPerPedalPress"] = True
@ctx.action_class("user")
class UserActions:
    """anki spaced repetition system overrides for pedal"""
    def north_up():
        actions.key("space")

    def east_up():
        actions.key("4")

    def west_up():
        actions.key("1")

    def east_north_down():
        actions.key("3")
    
    def north_west_down():
        actions.key("2")
