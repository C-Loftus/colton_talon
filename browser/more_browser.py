from talon import Module, Context, actions, clip

import webbrowser

mod = Module()


@mod.action_class
class Actions:
    def launch_new_tab_if_not_opened(website: str):
        """Launches a new tab if the website is not opened"""

        try:
            chrome = actions.user.get_running_app("Chrome")
            actions.user.switcher_focus_app(chrome)
        except:
            raise NotImplementedError("Firefox doesn't support a keyboard shortcut for tab search")

        actions.key("ctrl-l")
        actions.sleep(0.05)
        actions.insert("@tabs")
        actions.key("space")
        actions.user.paste(website)
        actions.key("enter")
        actions.sleep(0.5)
        actions.key("ctrl-a")
        actions.key("ctrl-c")
        actions.sleep(0.25)

        clipped_web = clip.text().strip()

        #this checks if nothing happened and then opens a new tab if nothing happened
        if TAB_SEARCH_RETURNED_NONE := (website.strip() == clipped_web):
            webbrowser.open(website)

        actions.key("ctrl-shift-home")