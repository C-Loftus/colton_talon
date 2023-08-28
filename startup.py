from talon import app, Context
import subprocess, os


def app_ready():
    current_dir = os.path.dirname(os.path.abspath(__file__) )

    def create_path(path):
        return os.path.join(current_dir, "..", path)

    repos = ["rango-talon", "cursorless-talon", "knausj_talon", "my_talon_scripts"]

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
            print(e)

    if no_updates:
        print("Your Talon User Directory is up to date!")

if os.name != 'nt':
    app.register("ready", app_ready)


game_controller_config = (
    "03000000c01600008704000011010000,"
    "Serial/Keyboard/Mouse/Joystick,"
    "platform:Linux,"
    "a:b1,b:b0,x:b2,y:b3,dpup:b4,"
)

# 03000000c01600008704000000000000,Serial/Keyboard/Mouse/Joystick,platform:Windows,a:b4,b:b3,x:b2,y:b1,dpup:b0,

# os.environ["SDL_GAMECONTROLLERCONFIG"] = game_controller_config
