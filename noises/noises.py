from talon import noise, ctrl, actions, ui, Context, scope
from talon_plugins import eye_mouse, eye_zoom_mouse
from talon_plugins.eye_mouse import config, toggle_camera_overlay, toggle_control
import talon
from talon import Module, actions

pop_lock = False
hiss_lock=False
mod = Module()

@mod.action_class
class Locks:
    
    # detect how long user has been working on the keyboard
    def lock_scroll():
        """
        Lock the hiss
        """
        global hiss_lock
        hiss_lock=True
    def lock_pop():
        """
        Lock the pop
        """
        global pop_lock
        print("pop lock")
        pop_lock=True
    def unlock_scroll():
        """
        Unlock the hiss
        """
        global hiss_lock

        hiss_lock=False
    def unlock_pop():
        """
        Unlock the pop
        """
        global pop_lock
        pop_lock=False

def check_youtube():
    try:
        t = ui.active_window().title.split(" - ")[-1].split(" — ")[0]
        return t
    except:
        return ""


def pop_handler(active: bool):
    dictation_mode = "dictation" in scope.get("mode")
    global pop_lock
    if not dictation_mode and not pop_lock:
            if ((eye_zoom_mouse.zoom_mouse.enabled == False) and (config.control_mouse == False)):
                ctrl.mouse_click(button=0, hold=16000)
                # print(list(scope.get("mode10"))[4])
    elif pop_lock:
        print("pop lock")
noise.register("pop", pop_handler)


def on_hiss(active: bool):
    dictation_mode = "dictation" in scope.get("mode")
    YouTube = check_youtube() == "YouTube"
    code = ui.active_app().name == "Code"
    docs = "Google Docs" in ui.active_window().title

    # print(f'{YouTube=} {code=} {docs=} {dictation_mode=}')
    global hiss_lock

    if not dictation_mode and \
        not YouTube and \
        not code and \
        not docs \
        and not hiss_lock:
        actions.user.mouse_scroll_down(amount=1.2)
    elif hiss_lock:
        print("hiss lock")
                    
noise.register("hiss", on_hiss)




# patterns.json
# 	"throttle": {
# 			"gluck": 0.9
# 		}	