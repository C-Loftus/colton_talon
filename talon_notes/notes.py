from sys import stdout
from talon import Module, actions, imgui
import sqlite3, os, time, shutil

mod = Module()
db = os.path.dirname(os.path.realpath(__file__)) + "/notes.db"

current_page = "general"

def getPageList():
    """Returns a list of all pages"""
    conn = sqlite3.connect(db)
    pages = []
    try:
        c = conn.cursor()
        c.execute("SELECT DISTINCT page FROM notes")
        for page in c.fetchall():
            pages.append(page[0])
    finally:
        conn.close()
    return pages


@imgui.open()
def gui(gui: imgui.GUI):

    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY,
        note TEXT,
        page TEXT
    )""")

    # check if there are any general pages 
    # if not, create one
    c.execute("SELECT * FROM notes WHERE page = 'general'") 
    if c.fetchone() is None:
        c.execute("INSERT INTO notes (page) VALUES (?)", ("general",))
        conn.commit()

    global current_page

    #  get all page names from the database and print them 
    # at the top of the window
    c.execute("SELECT DISTINCT page FROM notes")
    pages = c.fetchall()
    gui_page_list = ""
    for page in pages:
        if page[0] != current_page:
            gui_page_list += f"{ page[0] } | "

    gui.text(f' Current Page: {current_page} --- Others: {gui_page_list}')
    gui.line()

    # print all notes for the current page
    c.execute("SELECT * FROM notes")
    rows = c.fetchall()
    for row in rows:
        page_name = row[2]
        text = row[1]
        if page_name == current_page and (text != None and text != ""): 
            gui.text(f'{row[0]}: {row[1]}.')

    gui.spacer()
    if gui.button("Close"):
        gui.hide()


@mod.action_class
class Actions:
    def pencil_note(text: str):
        """Adds a note to the GUI"""
        global current_page
        page = current_page
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
            print(f'NOTES ERROR In erase_note: \'{e}\'')
        finally:
            conn.close()

        if gui.showing:
            # Hiding then showing prevents visual bugs
            gui.hide()
            gui.show()

    def trash_notes():
        """Removes all notes from the GUI"""
        try:
            os.remove(db)
        except FileNotFoundError:
            print("NOTES ERROR WHEN TRASHING ALL NOTES: No notes to erase")

        if gui.showing:
            gui.hide()
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

    def new_page(page: str):
        """Creates a new page"""
        page_list = getPageList()

        if page in page_list:
            print(f'NOTES: {page} is already a page')
            return
            
        global current_page
        current_page = page

        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            c.execute("""CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                note TEXT,
                page TEXT
            )""")
            c.execute("INSERT INTO notes (page) VALUES (?)", (page,))
            conn.commit()
        finally:
            conn.close()

        gui.hide()
        gui.show()



    def switch_page(page: str):
        """Switches the current page"""
        page_list = getPageList()
        print(page_list)

        if page not in page_list:
            print(f'NOTES: \'{page}\' is not a valid page')
            return

        global current_page
        current_page = page
        if gui.showing:
            gui.hide()
            gui.show()

        print(f'NOTES: Switched to {page} with{current_page=}{page_list=}')

    def erase_page(Page: str):
        """Removes a page from the database"""
        if Page == "general":
            print("NOTES: The general page itself cannot be deleted because it is the default page. However,  the associated notes will still be deleted")

        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            c.execute("DELETE FROM notes WHERE page = ?", (Page,))
            conn.commit()

            """Recomputes the primary key for the database"""
            c.execute("SELECT * FROM notes")
            rows = c.fetchall()

            # enumerate rows
            for index, row in enumerate(rows):
                c.execute("UPDATE = ? WHERE id = ?", (index, row[0]))
            conn.commit()
        except Exception as e:
            print(f'NOTES ERROR IN erase_page: \'{e}\'')
        finally:
            conn.close()
        global current_page
        current_page = "general"
        if gui.showing:
            gui.hide()
            gui.show()

    def backup_notes():
        """Exports all notes to a text file"""

        now = time.strftime("%Y-%m-%d")

        backups = os.path.join(os.path.dirname(__file__), "backups")
        if not os.path.exists(backups):
            os.mkdir(backups)

        # copy database to text file
        db_backup = os.path.join(backups, f"notes_{now}.db")
        shutil.copy(db, db_backup)

        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM notes")
            rows = c.fetchall()

            path = os.path.join(backups, f"notes_{now}.txt")
            with open(os.path.expanduser(path), "w") as f:
                for row in rows:
                    f.write(f'{row}\n')
        finally:
            conn.close()

    def log_notes():
        """Logs all notes In the talon log"""
        conn = sqlite3.connect(db)
        try:
            c = conn.cursor()
            c.execute("SELECT * FROM notes")
            rows = c.fetchall()
            print("Exporting notes...") 
            for row in rows:
                print(f'NOTES: {row}')
        finally:
            conn.close()

