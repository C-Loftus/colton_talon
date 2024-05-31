from talon import Context, Module

mod = Module()
ctx = Context()

mod.tag("asPedal", "Current input method can use pedal press commands")
mod.tag("asArduino", "Current input method uses arduino joystick commands")


isPedal = False

ctx.tags = ["user.asArduino"]


@mod.action_class
class Actions:
    def toggleAsPedal():
        """Toggle asPedal Tag"""
        global isPedal
        if isPedal:
            ctx.tags = ["user.asArduino"]
        else:
            ctx.tags = ["user.asPedal"]

        isPedal = not isPedal
