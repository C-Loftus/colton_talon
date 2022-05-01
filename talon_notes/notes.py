
from talon import Module, actions, imgui
import webbrowser


mod = Module()

@imgui.open()
def gui(gui: imgui.GUI):
    gui.text("snippets")
    gui.line()


    gui.text("{}".format("test"))

    gui.spacer()
    if gui.button("Snip close"):
        gui.hide()



@mod.action_class
class Actions:
    def add_note(text: str):
        """Adds a note to the snippet UI"""
        gui.text("{}".format(text))
        gui.show()

    def toggle_notes():
        """Toggles UI for available snippets"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()
    def hide_notes():
        """Hides the snippet UI"""
        gui.hide()

