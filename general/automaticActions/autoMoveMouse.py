from talon import Module, cron, actions, ctrl, ui, Context
import time

mod = Module()

job = None

def mouse_move_random():
    """move the mouse cursor to the center of the currently active window"""
    actions.user.notify("moving mouse automatically")
    print("moving mouse automatically")
    rect = ui.active_window().rect
    ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))
    time.sleep(0.75)
    ctrl.mouse_move(rect.left, rect.top)
    time.sleep(0.75)
    ctrl.mouse_move(rect.left + (rect.width), rect.top + (rect.height))



@mod.action_class
class act: 
    def toggle_auto_move_mouse():
        """Toggle auto move mouse"""
        actions.user.notify("moving mouse automatically")
        global job
        if job:
            job.cancel()
        else:
            job =  cron.interval("50s", mouse_move_random)
            
    def mouse_move_center_active_window():
        """move the mouse cursor to the center of the active window"""

        rect = ui.active_window().rect
        ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))

    def mouse_move_center_specific_window(window_name: str):
        """move the mouse cursor to the center of a specific window"""

        windows = ui.windows()
        for win in windows:
            application_name = win.app.name
            if window_name in application_name:
                rect = win.rect
                ctrl.mouse_move(rect.left + (rect.width / 2), rect.top + (rect.height / 2))
                return 