import contextlib
from threading import Lock
import os, pathlib
from typing import ContextManager, Generic, TypeVar
from talon import Module, actions, Context, scope, clip

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

