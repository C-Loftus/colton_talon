 #  this file defines the function that is called within 
 # my change to the knausj focus command

from talon import Module, actions, ui, app
import time

mod = Module()

@mod.action_class
class focus:

    def jump_workspace_and_switch_focus(my_application: str):
        """ jump_workspace_and_switch_focus """
        app_list=ui.apps()
        workspace = 1
        for app in app_list:
            if app.name==my_application:
                workspace = app.active_window.workspace
                ui.switch_workspace(workspace)
                 # if switch happens too fast you will ignore the focus
                time.sleep(0.1)
                app.focus()
                break