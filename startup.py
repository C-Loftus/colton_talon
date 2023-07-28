from talon import app, Context
import subprocess, os


def app_ready():
    current_dir = os.path.dirname(os.path.abspath(__file__) )

    def create_path(path):
        return os.path.join(current_dir, os.path(".."), path)

    repos = ["rango-talon", "cursorless-talon", "knausj_talon"]

    paths = map(create_path, repos)

    no_updates = True

    for path in paths:
        try:
            # Change the current working directory to the file's directory
            os.chdir(path)

            # Check if there are any new changes
            output = subprocess.check_output(['git', 'status', '-uno'], stderr=subprocess.STDOUT)
            output = output.decode('utf-8')

            # If the output contains "Your branch is behind", there are new changes
            if 'Your branch is behind' in output:
                app.notify(body=f"New changes are available for {path}")
                no_updates = False

        except subprocess.CalledProcessError as e:
            # Error occurred while executing git command
            print(f"e")

    if no_updates:
        print("Your Talon User Directory is up to date!")

if os.name != 'nt':
    app.register("ready", app_ready)
