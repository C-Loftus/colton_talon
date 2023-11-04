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
