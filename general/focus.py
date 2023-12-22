 #  this file defines the function that is called within 
 # my change to the knausj focus command

from talon import Module, actions, ui, app
import time, webbrowser

mod = Module()

@mod.action_class
class focus:

    def jump_workspace_and_switch_focus(my_application: str):
        """ jump_workspace_and_switch_focus """
        app_list=ui.apps()
        workspace = 1
        for app in app_list:
            if app.name==my_application:
                workspace = app.active_window.workspace
                ui.switch_workspace(workspace)
                 # if switch happens too fast you will ignore the focus
                time.sleep(0.1)
                app.focus()
                break
    


    # def open_or_focus_tab(url: str):
    #     """ Open the website if it is not already open otherwise focus the running tab """

    #     def get_base_name(url):
    #         # Remove any leading/trailing whitespaces and trailing slashes
    #         url = url.strip().rstrip("/")

    #         # Check if the URL starts with "http://" or "https://"
    #         if url.startswith("http://"):
    #             url = url[7:]
    #         elif url.startswith("https://"):
    #             url = url[8:]

    #         # Find the first occurrence of '/' after removing the protocol part
    #         index = url.find("/")
    #         if index != -1:
    #             # If '/' is found, extract the base name
    #             base_name = url[:index]
    #         else:
    #             # If no '/', the entire URL is considered the base name
    #             base_name = url

    #         return base_name

    #     def find_base_url_tab(base_url):
    #         # Get a list of open browser windows
    #         browser_windows: webbrowser.BaseBrowser = webbrowser.get()
            
    #         # Check if the base URL is already open in any tab
    #         for window in browser_windows:
    #             for tab in window.tabs:
    #                 if base_url in tab.url:
    #                     return window, tab

    #         return None, None

    #     # Check if the base URL is already open in any tab
    #     window, tab = find_base_url_tab(get_base_name(url))
        
    #     # If the base URL is already open, focus on the tab
    #     if window and tab:
    #         window.activate_tab(tab)
    #     else:
    #         # If the base URL is not open, open a new tab
    #         webbrowser.open(url)
