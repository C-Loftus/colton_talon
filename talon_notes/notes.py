
from talon import Module, actions, imgui
import os
import sqlite3

mod = Module()
db = os.path.dirname(os.path.realpath(__file__)) + "/notes.db"
text_path = os.path.dirname(os.path.realpath(__file__)) + "/notes.txt"

@imgui.open()
def gui(gui: imgui.GUI):

    gui.text("Notes")
    gui.line()

    # if database doesn't exist, create it
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        note TEXT
    )""")
    # print all rows in table
    c.execute("SELECT * FROM notes")
    rows = c.fetchall()
    for row in rows:
        gui.text(f'{row[0]}: {row[1]}')

    gui.spacer()
    if gui.button("Close"):
        gui.hide()

@mod.action_class
class Actions:
    def add_note(text: str):
        """Adds a note to the GUI"""

        # add string to database
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("""CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY,
            note TEXT
        )""")
        c.execute("INSERT INTO notes (note) VALUES (?)", (text,))
        conn.commit()
        conn.close()

        gui.hide()
        gui.show()


    def erase_note(primary_key: str):
        """Removes a note from the GUI"""
        try:
            conn = sqlite3.connect(db)
            c = conn.cursor()
            c.execute("DELETE FROM notes WHERE id = ?", (primary_key,))
            conn.commit()

            """Recomputes the primary key for the database"""
            c.execute("SELECT * FROM notes")
            rows = c.fetchall()

            # enumerate rows
            for index, row in enumerate(rows):
                c.execute("UPDATE = ? WHERE id = ?", (index, row[0]))
            conn.commit()
            conn.close()        
        except Exception as e:
            print(e)
        if gui.showing:
            # Hiding then showing prevents visual bugs
            gui.hide()
            gui.show()

    def trash_note():
        """Removes all notes from the GUI"""
        try:
            os.remove(db)
        except FileNotFoundError:
            print("No notes to erase")

    def toggle_notes():
        """Toggles Available notes"""
        if gui.showing:
            gui.hide()
        else:
            gui.show()
    def hide_notes():
        """Hides notes"""
        gui.hide()

    def export_notes():
        """Exports all notes to a text file"""
        conn = sqlite3.connect(db)
        c = conn.cursor()
        c.execute("SELECT * FROM notes")
        rows = c.fetchall()
        with open(os.path.expanduser(text_path), "w") as f:
            print("Exporting notes...") 
            for row in rows:
                f.write(f'{row[0]}: {row[1]}\n')
                print(f'{row[0]}: {row[1]}')
        conn.close()