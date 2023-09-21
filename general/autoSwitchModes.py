from talon import actions,ui, scope
import time, os

COMMAND_MODE_APPLICATIONS=['Visual Studio Code']
previous_mode: str = None
SLEEP_MODE_APPLICATIONS = []

# auto dismiss popups on work computer
def dismiss_popup(application):
    if "XamlAction" in application.name and os.name == 'nt':
        actions.insert("This is a bug in Delinea caused by a misrecognition of Talon. This is auto dismissed")
        time.sleep(.5)
        actions.key("tab")
        actions.key("enter")
        actions.key("enter")


def enable_mixed_mode():
    global previous_mode
    previous_mode = "mixed"
    actions.mode.disable("sleep")
    actions.mode.enable("dictation")
    actions.mode.enable("command")

def enable_command_mode():
    global previous_mode
    previous_mode = "command"
    actions.mode.disable("sleep")
    actions.mode.disable("dictation")
    actions.mode.enable("command")

def on_app_switch(application):
    dismiss_popup(application)
    
    if "sleep" not in scope.get("mode"):
        global previous_mode
        for app in COMMAND_MODE_APPLICATIONS: 
            if app in application.name or application.name in app:
                enable_command_mode()
                print('auto switched to command mode')
                return
        else:
            if previous_mode != "mixed":
                enable_mixed_mode()
                print('auto switched to mixed mode')

ui.register("app_activate", on_app_switch)