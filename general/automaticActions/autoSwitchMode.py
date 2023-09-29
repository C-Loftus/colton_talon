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
    # print(ctx.tags, list(ctx.tags), "user.auto_switch_mode" in list(ctx.tags))
    if "user.auto_switch_mode" not in list(ctx.tags) or "sleep" in scope.get("mode"):
        return

    global previous_mode
    for app in COMMAND_MODE_APPLICATIONS: 
        if app in application.name or \
            application.name in app and actions.code.language() != "markdown":
            enable_command_mode()
            return
    else:
        if previous_mode != "mixed":
            enable_mixed_mode()

def switcher():
    ui.register("app_activate", on_app_switch)

# we need to wait until it is loaded since otherwise it could fail when a mode is not defined during startup
app.register("ready", switcher )
