
from sys import stdout
from talon import Module, actions, imgui
import sqlite3, os, time

mod = Module()
db = os.path.dirname(os.path.realpath(__file__)) + "/notes.db"
text_path = os.path.dirname(os.path.realpath(__file__)) + "/notes.txt"

current_page = "General Notes"

@imgui.open()
def gui(gui: imgui.GUI):

    # if database doesn't exist, create it
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        note TEXT
        page TEXT
    )""")

    gui.text("Notes")
    gui.line()
    c.execute("SELECT * FROM notes")

    rows = c.fetchall()


    ROW_WIDTH = 80

    # for row in rows:
    #     total_chars = len(row[1])

    #     for index in range(0, total_chars, ROW_WIDTH):
    #         offset = total_chars if index + ROW_WIDTH >= total_chars else ROW_WIDTH

    #         primary_key = str(row[0]) + ": "
    #         no_overflow = index == 0
    #         start = primary_key if no_overflow else "   "

    #         gui.text(f'{start}{row[1][index:index+offset]}')

    for row in rows:
        gui.text(f'{row[0]}: {row[1]}. {row[2]}')

    gui.spacer()
    if gui.button("Close"):
        gui.hide()


@mod.action_class
class Actions:
    def add_note(text: str, page: str = "General"):
        """Adds a note to the GUI"""

        # add string to database
        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            # create database with columns id, note, page if it doesn't exist
            c.execute("""CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                note TEXT,
                page TEXT
            )""")
            # add note to database
            
            # insert text and page into database
            c.execute("INSERT INTO notes (note, page) VALUES (?, ?)", (text, page))

            conn.commit()
        finally:
            conn.close()

        # hide then show to prevent visual bugs
        gui.hide()
        gui.show()


    def erase_note(primary_key: str):
        """Removes a note from the GUI"""
        conn = sqlite3.connect(db)
        try:
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
        except Exception as e:
            print(f'NOTES ERROR: {e}')
        finally:
            conn.close()

        if gui.showing:
            # Hiding then showing prevents visual bugs
            gui.hide()
            gui.show()

    def trash_note():
        """Removes all notes from the GUI"""
        try:
            os.remove(db)
        except FileNotFoundError:
            print("NOTES: No notes to erase")

        if gui.showing:
            gui.show()

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
        # get current time
        now = time.strftime("%Y-%m-%d_%H-%M-%S")

        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM notes")
            rows = c.fetchall()
            with open(os.path.expanduser(text_path + now ), "w") as f:
                print("Exporting notes...") 
                for row in rows:
                    f.write(f'{row[0]}: {row[1]}\n')
                    print(f'{row[0]}: {row[1]}')
        finally:
            conn.close()


