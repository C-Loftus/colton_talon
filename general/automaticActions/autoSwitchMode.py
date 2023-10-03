from talon import actions,ui, scope, app, Context, Module
import time, os

mod = Module()
mod.tag("auto_switch_mode", desc="auto switch mode based on application")
ctx = Context()

ctx.tags = ["user.auto_switch_mode"]
tags: set[str] = set()


def add_tag(tag: str):
    tags.add(tag)
    ctx.tags = list(tags)


def remove_tag(tag: str):
    tags.discard(tag)
    ctx.tags = list(tags)

def toggle_tag(tag: str)-> str :
    if tag in ctx.tags:
        remove_tag(tag)
        return "removed"
    else:
        add_tag(tag)
        return "enabled"

@mod.action_class
class mods():
    def toggle_auto_switch_mode():
        """Toggle auto switch mode"""
        resp = toggle_tag("user.auto_switch_mode")
        actions.user.notify(f"auto switch mode is now: {resp}")



previous_mode: str = None
SLEEP_MODE_APPLICATIONS = []

# auto dismiss popups on work computer.
def dismiss_popup(application):
    if "XamlAction" in application.name and os.name == 'nt':
        actions.insert("This is a bug in Delinea caused by a misrecognition of Talon. This is auto dismissed")
        time.sleep(.5)
        actions.key("tab")
        actions.key("enter")
        actions.key("enter")


def enable_mixed_mode():
    global previous_mode
    previous_mode = scope.get("mode")
    actions.mode.disable("sleep")
    actions.mode.enable("dictation")
    actions.mode.enable("command")

def enable_command_mode():
    global previous_mode
    previous_mode = scope.get("mode")
    actions.mode.disable("sleep")
    actions.mode.disable("dictation")
    actions.mode.enable("command")


def do_update():
    if "user.auto_switch_mode" not in list(ctx.tags):
        return False

    if scope.get("mode") == "sleep":
        return False

    match actions.code.language():
        case "markdown":
            return False
        
    return True

def on_title_switch(window):
    if not do_update():
        return
        

    MIXED_MODE_APPLICATIONS=["app.slack.com", "Microsoft Teams"]
    for app_name in MIXED_MODE_APPLICATIONS:

        if app_name in ui.active_window().title:

            enable_mixed_mode()
            return
    
    enable_command_mode()
        # match ui.active_window().:
        #     case [*_, "holidays"]:
        #         return True
        #     case [*_, "workday"]:
        #         return False

#course grained updates according to application name and not specific titles
def on_app_switch(application):

    if not do_update():
        return

    COMMAND_MODE_APPLICATIONS=['Visual Studio Code']
    for app in COMMAND_MODE_APPLICATIONS: 

        if app in application.name:
            enable_command_mode()
            return
        
        title =  str(ui.active_window().title).lower()
        if "modern calling" in title:
            enable_command_mode()
            return


def switcher():
    ui.register("app_activate", on_app_switch)
    ui.register("win_title", on_title_switch)
    ui.register("app_activate", dismiss_popup)


# we need to wait until it is loaded since otherwise it could fail when a mode is not defined during startup
app.register("ready", switcher )
