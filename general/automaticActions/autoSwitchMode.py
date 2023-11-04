from talon import actions,ui, scope, app, Context, Module, cron
import time, os

mod = Module()
mod.tag("auto_switch_mode", desc="auto switch mode based on application")
ctx = Context()

ctx.tags = ["user.auto_switch_mode"]
tags: set[str] = set()

STRECHLY_RUNNING = True

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





def do_update():

    if "user.auto_switch_mode" not in list(ctx.tags):
        return False

    if "sleep" in scope.get("mode"):
        return False

    return True

def on_title_switch(window):
    if not do_update():
        return
        

    window_title = ui.active_window().title

    if "Microsoft Teams" in window_title:

        if "?ctx=chat" in window_title:
            actions.user.enable_mixed_mode()
            return
            

        actions.user.enable_command_mode()
        return
    
    mixed_websites = ["app.slack.com", "outlook.office.com", "chat.openai.com"]

    for website in mixed_websites:
        if website in window_title:
            actions.user.enable_mixed_mode()
            return

    if 'Visual Studio Code' in window_title: 
        if actions.code.language() == "markdown":
            actions.user.enable_mixed_mode()

        else:
            actions.user.enable_command_mode()
        return    
    
    global STRECHLY_RUNNING
    if not STRECHLY_RUNNING and os.name == 'nt':

        def start_strechly():
            actions.key(STRETCHLY := "super-9")
            global STRECHLY_RUNNING
            STRECHLY_RUNNING = True
            actions.user.notify("started stretchy")

        cron.after("5s", start_strechly)
        

#course grained updates according to application name and not specific titles
def on_app_switch(application):

    if not do_update():
        return


    # actions.user.notify(f'{actions.code.language(), application.name}')

    # The Linux name is just code but on windows it seems to be visual studio code
    if 'Code' in application.name: 
        if actions.code.language() == "markdown":
            actions.user.enable_mixed_mode()

        else:
            actions.user.enable_command_mode()
            # actions.user.notify(f'{actions.code.language()}')
        return    
    
    
    title =  str(ui.active_window().title).lower()
    if "modern-calling" in title and os.name == 'nt':
        global STRECHLY_RUNNING
        # kill the stretchy application
        try:
            os.system("taskkill /f /im Stretchly.exe")
            actions.user.notify("killed stretchy")
            STRECHLY_RUNNING = False
        except:
            actions.user.notify("could not kill stretchy")
            STRECHLY_RUNNING = True

        actions.user.enable_command_mode()
        return


def switcher():
    match os.name:
        case 'nt':
            ui.register("app_activate", dismiss_popup)
        case _: 
            pass

    ui.register("app_activate", on_app_switch)
    ui.register("win_title", on_title_switch)


# we need to wait until it is loaded since otherwise it could fail when a mode is not defined during startup
app.register("ready", switcher )




