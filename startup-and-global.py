from talon import app, Context, actions, ui
import subprocess, os, time

if os.name == 'nt':
    import win32gui
import os

def get_windows_running_apps():
    
    #Remove these apps from the list since they aren't necessary and can't be called with keyboard shortcuts anyways
    FILTER_THESE = ['Microsoft Text Input Application', 'Windows Shell Experience Host', 'Search', 'Cortana', "Start"]
    taskbar_apps = []

    def callback(hwnd, lParam):
        if win32gui.IsWindowVisible(hwnd):
            title = win32gui.GetWindowText(hwnd)
            if title:
                taskbar_apps.append(title)

    # Enumerate all top-level windows
    win32gui.EnumWindows(callback, 0)

    # Filter out empty titles and duplicates
    taskbar_apps = list(filter(None, taskbar_apps))
    taskbar_apps = [x for x in taskbar_apps if x not in FILTER_THESE]

    taskbar_apps = list(set(taskbar_apps))

    return taskbar_apps


def check_git():
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
    def app_ready_unix():
        check_git()
    app.register("ready", app_ready_unix)

if os.name == 'nt':
    def app_ready_windows():
        # for some reason this application doesn't auto start natively 
        # through windows so we have to just press the key
        actions.key(STRETCHLY := "super-9")
    app.register("ready", app_ready_windows)

# auto dismiss popups on work computer
def on_app_switch(application):
    if "XamlAction" in application.name:
        actions.insert("This is a bug in Delinea caused by a misrecognition of Talon. This is auto dismissed")
        time.sleep(.5)
        actions.key("tab")
        actions.key("enter")
        actions.key("enter")

ui.register("app_activate", on_app_switch)

game_controller_config = (
    "03000000c01600008704000011010000,"
    "Serial/Keyboard/Mouse/Joystick,"
    "platform:Linux,"
    "a:b1,b:b0,x:b2,y:b3,dpup:b4,"
)

# 03000000c01600008704000000000000,Serial/Keyboard/Mouse/Joystick,platform:Windows,a:b4,b:b3,x:b2,y:b1,dpup:b0,

# os.environ["SDL_GAMECONTROLLERCONFIG"] = game_controller_config
