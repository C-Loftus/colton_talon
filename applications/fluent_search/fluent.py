from talon import Context, Module, actions, app, ui

# SOURCE: https://github.com/nriley/talon_community/blob/nriley/apps/fluent_search/fluent_search.py 

mod = Module()
ctx = Context()
ctx.tags = []
ctx.matches = """
os: windows
"""

mod.tag("fluentSearchHintsOpen", "Current input method can use pedal press commands")

isSearching = False
        
def wait_for_fluent_search_window():
    for _ in range(10):
        if ui.active_app().name == "FluentSearch":
            return True
        actions.sleep("50ms")
    
    app.notify("Gave up while waiting for Fluent Search")
    return False

@mod.action_class
class Action:
    def fluent_search(text: str):
        """Searches using Fluent Search"""

    def fluent_search_in_app(text: str, submit: bool):
        """Searches using Fluent Search’s In-app Search"""

    def toggleFluentSearchTags():
        """Toggle fluentsearch label Tag"""

@ctx.action_class("user")
class UserActions:
    def toggleFluentSearchTags():
            """Toggle asPedal Tag"""
            actions.key("ctrl-alt-;")
            global isSearching
            if isSearching:
                ctx.tags = ["user.fluentSearchHintsOpen"]
            else:
                ctx.tags = []
            
            isSearching = not isSearching


    def fluent_search(text: str):
        # XXX can't use app.focus() and unaware of any other way to
        # automate the way we do with LaunchBar
        # If you have a different search keyboard shortcut configured,
        # replace ctrl-alt-space with it below.
        actions.key("ctrl-alt-space")
        wait_for_fluent_search_window()
        actions.key("backspace")
        if "\t" in text:
            plugin, text = text.split("\t", 1)
            actions.insert(plugin + "\t")
        actions.user.paste(text)

    def fluent_search_in_app(text: str, submit: bool):
        actions.key("alt-shift-/")
        wait_for_fluent_search_window()
        actions.user.paste(text)
        if submit:
            actions.key("enter")