from talon import Context, Module, actions

mod = Module()
ctx_sleep = Context()


ctx_sleep.matches = r"""
mode: sleep
os: linux
os: windows
os: mac
"""

@ctx_sleep.action_class("speech")
class ActionsSleepMode:
    def disable():
        """In community, there is an app notify here. However, I don't care about this. Just ignore it"""
        pass