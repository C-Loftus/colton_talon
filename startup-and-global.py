import os
import subprocess

from talon import actions, app, cron

def check_git():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(current_dir)
    repos = os.listdir(parent_dir)

    def create_path(path):
        return os.path.join(current_dir, "..", path)

    paths = map(create_path, repos)

    no_updates = True

    for path in paths:
        try:
            # Change the current working directory to the file's directory
            os.chdir(path)

            # Check if there are any new changes
            output = subprocess.check_output(
                ["git", "status", "-uno"], stderr=subprocess.STDOUT
            )
            output = output.decode("utf-8")

            # If the output contains "Your branch is behind", there are new changes
            if "Your branch is behind" in output:
                app.notify(body=f"New changes are available for {path}")
                print(f"New changes are available for {path}")
                no_updates = False

        except subprocess.CalledProcessError as e:
            # Error occurred while executing git command
            print(e)

    if no_updates:
        print("Your Talon User Directory is up to date!")


def disconnect_eye_tracker():
    try:
        actions.user.mouse_sleep()
        actions.user.disconnect_ocr_eye_tracker()
    except:  # noqa: E722
        # if the eye tracker is already disconnected, just pass
        # we don't care about errors here
        pass


def auto_actions_on_startup():
    cron.after("4s", disconnect_eye_tracker)
    if os.name == "posix":
        check_git()

app.register("ready", auto_actions_on_startup)
