## THIS FILE USES PLAIN TEXT INSTEAD OF A DATABASE

# from talon import Module, actions, imgui
# import os
# import sqlite3

# mod = Module()
# path = os.path.dirname(os.path.realpath(__file__)) + "/notes.txt"

# @imgui.open()
# def gui(gui: imgui.GUI):
#     gui.text("Notes")
#     gui.line()

#     # if file doesn't exist, create it
#     if not os.path.isfile(path):
#         with open(path, "w") as f:
#             f.write("")

#     with open(os.path.expanduser(path), "r") as f:
#         for line in f.readlines():
#             gui.text(line.strip())

#     gui.spacer()
#     if gui.button("Close"):
#         gui.hide()

# @mod.action_class
# class Actions:
#     def add_note(text: str):
#         """Adds a note to the GUI"""
#         # get number of lines in file

#         with open(path, "a+") as f:
#             f.write(f"\n{text}")
#         gui.show()

#     def erase_note():
#         """Removes a note from the GUI"""
#         gui.hide()
#         try:
#             os.remove(path)
#         except FileNotFoundError:
#             print("No notes to erase")

#     def toggle_notes():
#         """Toggles UI for available snippets"""
#         if gui.showing:
#             gui.hide()
#         else:
#             gui.show()
#     def hide_notes():
#         """Hides the snippet UI"""
#         gui.hide()