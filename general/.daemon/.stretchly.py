import time
import subprocess
import pygetwindow as gw

def run_command(command):
    subprocess.run(command, shell=True)

PATH = "C:\\Users\\cloftus\\AppData\\Local\\Programs\\Stretchly\\Stretchly.exe"

def main():
    paused=False

    while True:
        active_window = gw.getActiveWindow()
        print(f'{active_window=}, {paused=}')
        if active_window is not None:
            current_window_title = active_window.title

            # signifies a teams meeting in progress
            if "modern-calling" in current_window_title and not paused:
                run_command(f'{PATH} pause')
                paused=True
            elif paused:
                run_command(f'{PATH} resume')
                paused = False

        time.sleep(2)

if __name__ == "__main__":
    main()


# from talon import Module, actions, cron, scope, Context, settings
# import time

# mod = Module()
# ctx = Context()
# ctx.matches = r"""
# os: windows
# app: microsoft_teams and
# title: /calling/
# """

# PATH = "C:\\Users\\cloftus\\AppData\\Local\\Programs\\Stretchly\\Stretchly.exe"

# actions.user.system_command_nb(f'{PATH} pause')



# force_synchronous = mod.setting(
#     "force_synchronous",
#     type=bool,
#     default=False, 
#     desc="force_synchronous",
# )

# #  turns just the center pedal into a synchronous option
# force_synchronous_center = mod.setting(
#     "force_synchronous_center",
#     type=bool,
#     default=True,
#     desc="force_synchronous_center",
# )


# cron.interval("16ms", on_interval)


# @mod.action_class
# class Actions:

