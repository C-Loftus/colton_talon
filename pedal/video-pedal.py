from talon import Context, actions

ctx = Context()
ctx.matches = """title: /watch/
title: /soundcloud/
"""

@ctx.action_class("user")
class CodeActions:
    
    def left_pedal():
        pass
        # actions.key("voldown")

    def right_pedal():
        pass
        # actions.key("volup")

    def center_pedal():
        pass

    def left_pedal_up():
        actions.key("voldown")
        pass
    def right_pedal_up():
        actions.key("volup")

        pass
    def center_pedal_up():
        pass



    
    