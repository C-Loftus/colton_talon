from talon import Module, actions, ui, ctrl, scope, app
import time

mod = Module()

@mod.action_class
class HotKey:
    
    def switch_app_and_mic():
        """ Switch the application"""
        name=ui.active_app().name
        try:
            actions.user.switcher_focus('zoom')

            time.sleep(.1)

            ctrl.key_press(key="a", alt=True)
        except:
            pass

        if "sleep" in scope.get("mode"):
            actions.speech.enable()
            app.notify("Now Woken Up")
        else:
            app.notify("Now Sleeping")
            actions.speech.disable()

    def mute_zoom_start_talon():
        """ Mute Zoom and start Talon"""
        actions.user.switcher_focus("zoom")
        time.sleep(.5)
        ctrl.key_press(key="a", alt=True)
        actions.speech.enable()

    def unmute_zoom_stop_talon():
        """ Unmute Zoom and stop Talon"""
        actions.user.switcher_focus("zoom")
        ctrl.key_press(key="a", alt=True)
        actions.speech.disable()