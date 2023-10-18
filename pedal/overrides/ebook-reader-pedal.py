from talon import Context, Module, actions

ctx = Context()
ctx.matches = r"""
title: /e-book viewer/i
"""


ctx.settings["user.oneActionPerPedalPress"] = True

@ctx.action_class("user")
class Actions:



    def left_up():
        actions.key('up')


    def right_up():
        actions.key(GO_UP_ENTIRE_SPLIT_PAGE_LAYOUT := 'down')

    # def center_up():
    #     actions.key("space")
        
