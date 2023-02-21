from talon import Module, actions

mod = Module()

@mod.action_class
class Actions:

    def left_pedal():
        """Left pedal"""
        actions.user.mouse_scroll_down_continuous()
    def right_pedal():
        """Right pedal"""
        actions.user.mouse_scroll_up_continuous()
    def center_pedal():
        """Center pedal"""
        # actions.user.mouse_scroll_stop()
        pass


    def left_pedal_up():
        """Left pedal up"""
        actions.user.mouse_scroll_stop()
    def right_pedal_up():
        """Right pedal up"""
        actions.user.mouse_scroll_stop()
    def center_pedal_up():
        """Center pedal up"""
        # actions.user.mouse_scroll_stop()
        pass