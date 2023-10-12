from talon import Context, Module, actions, settings, scope

ctx = Context()
ctx.matches = """app: vscode
not title: /html/
not tag: user.controlTabsWithPedal
"""

ctx.settings["user.oneActionPerPedalPress"] = False

ctx.tags = []
pedal_scroll_amount = settings.get("user.pedal_scroll_amount") if settings.get("user.pedal_scroll_amount") else 0.2

jump = False

display = False


def update_tag(ctx, tag):
    new_tags = set(ctx.tags)
    if tag in new_tags:
        new_tags.remove(tag)
    else:
        new_tags.add(tag)
    ctx.tags = frozenset(new_tags)

@ctx.action_class("user")
class Actions:

    def left_right_down():
        """Left and Right pedal"""
        global jump, display
        jump = not jump
        display = False
        print("Switching jump mode to", jump)


    def left_center_down():
        """Left and Center pedal"""
        global display, jump
        display = not display
        jump = False
        print("Switching display mode to", display)

    def center_right_down():
        """Center and Right pedal"""
        # update_tag(ctx, "pedal.scroll")


    def left_up():
        """Left pedal"""

        if display:
            actions.user.vscode("workbench.action.toggleSidebarVisibility")
            return

    def right_up():
        """Right pedal"""
        if display:
            actions.user.vscode("workbench.action.terminal.toggleTerminal")
            return


    def center_up():
        """Center pedal"""
        if display:
            actions.app.tab_next()
            return
        else:
            modes = scope.get("mode")
            if "sleep" in modes:
                # mode = "sleep"
                actions.speech.enable()
            else:    
                actions.speech.disable()


        


    def left_down():
        if not settings.get("user.oneActionPerPedalPress"):
            actions.user.mouse_scroll_down(pedal_scroll_amount)

    def right_down():
        if not settings.get("user.oneActionPerPedalPress"):
            actions.user.mouse_scroll_up(pedal_scroll_amount)

    def reset_pedal_state():
        """called when the center pedal is held down"""
        ctx.tags = []
        ctx.settings['user.pedal_scroll_amount'] = 0.2
