from typing import ContextManager
from talon import Module, actions, Context, scope, clip, ui, cron

mod = Module()
ctx = Context()

tags: set[str] = set()

def add_tag(tag: str):
    tags.add(tag)
    ctx.tags = list(tags)


def remove_tag(tag: str):
    tags.discard(tag)
    ctx.tags = list(tags) 




# Make the Mutex generic over the value it stores.
# In this way we can get proper typing from the `lock` method.
# class Mutex(Generic[T:=TypeVar("T")]):
#   # Store the protected value inside the mutex 
#   def __init__(self, value: T):
#     # Name it with two underscores to make it a bit harder to accidentally
#     # access the value from the outside.
#     self.__value = value
#     self.__lock = Lock()

#   # Provide a context manager `lock` method, which locks the mutex,
#   # provides the protected value, and then unlocks the mutex when the
#   # context manager ends.
#   @contextlib.contextmanager
#   def lock(self) -> ContextManager[T]:
#     self.__lock.acquire()
#     try:
#         yield self.__value
#     finally:
#         self.__lock.release()
# # Create a mutex wrapping the data
# mutex = Mutex([])

# # Lock the mutex for the scope of the `with` block
# with mutex.lock() as value:
#   # value is typed as `list` here
#   value.append(1)


@mod.action_class
class Actions:
    # def toggle_tag(tag:str):
    #     '''toggle a tag'''
    #     if tag in ctx.tags:
    #         remove_tag(tag)
    #     else:
    #         add_tag(tag)

    def enable_mixed_mode():
        """enable mixed mode"""
        actions.mode.disable("sleep")
        actions.mode.enable("dictation")
        actions.mode.enable("command")

    def enable_command_mode():
        """enable mixed mode"""
        actions.mode.disable("sleep")
        actions.mode.disable("dictation")
        actions.mode.enable("command")

    def toggle_sleep_mode():
        """toggle sleep mode"""
        modes = scope.get("mode")
        if "sleep" in modes:
            # mode = "sleep"
            actions.speech.enable()
        else:    
            actions.speech.disable()    

    def focus_chrome():
        """focus chrome"""
        chrome = actions.user.get_running_app("Chrome")
        actions.user.switcher_focus_app(chrome)

    def focus_vscode():
        """focus vscode"""
        vscode = actions.user.get_running_app("Code")
        actions.user.switcher_focus_app(vscode)

    def switch_between_code_and_chrome():
        """switch between code and chrome"""
        active_app = ui.active_app().name       
        if "Code" in active_app:
            actions.user.focus_chrome()
        elif "Chrome" in active_app:
            actions.user.focus_vscode()
        else:
            actions.user.focus_chrome()
        actions.sleep("100ms")
        # actions.key("escape")

    def grab_browser_window_slow():
        """grab browser window and wait for the pop up to disappear after going full screen"""
        actions.key("f11")
        actions.sleep(6)
        actions.user.screenshot_window_clipboard()
        actions.key("f11")

    def return_to_current_app_after(seconds: int): 
        """Return to the current app after a certain ones seconds"""
        active_app = ui.active_app().name
        saved_application= actions.user.get_running_app(active_app)
        
        def return_to_app():
            try:
                actions.user.switcher_focus_app(saved_application)
            except:
                actions.user.notify("return to app failed")
                print(f'Could not return to {saved_application}')

        cron.after(cron.seconds_to_timespec(seconds) , return_to_app)