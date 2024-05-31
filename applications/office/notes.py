import tempfile

from talon import Context, Module, actions, clip

mod = Module()

NOTE_PATH = None


BACKUP = None


@mod.action_class
class Actions:
    def create_note():
        """Creates a new note"""
        global NOTE_PATH
        NOTE_PATH = tempfile.mktemp(suffix=".md")

    def append_to_note(text: str):
        """Appends text to the end of the note"""
        global NOTE_PATH
        if not NOTE_PATH:
            actions.user.create_note()
        with open(NOTE_PATH, "a") as f:
            f.write(text)
            f.write("\n")

    def copy_note():
        """Copies the contents of the note to the clipboard"""
        global NOTE_PATH
        if not NOTE_PATH:
            return
        with open(NOTE_PATH, "r") as f:
            clip.set_text(f.read())
            global BACKUP
            BACKUP = f.read()

    def clear_note():
        """Clears the note"""
        global NOTE_PATH
        if not NOTE_PATH:
            return
        with open(NOTE_PATH, "w") as f:
            global BACKUP
            BACKUP = f.read()
            f.write("")

    def copy_backup_note():
        """Copies the contents of the note to the clipboard"""
        global BACKUP
        if not BACKUP:
            return
        clip.set_text(BACKUP)
