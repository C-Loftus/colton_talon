from talon import Module, Context , actions

import time
import sys


import tempfile

ctx = Context()
mod = Module()


functions = [
    # actions.user.east_north_west_down.__call__,
    "user.center_east_down",
    "user.east_west_down",
    "user.left_center_down",
    "user.west_down",
    "user.east_down",
    "user.center_down",
    "user.west_up",
    "user.east_up",
    "user.north_up"
]

@mod.action_class
class UserActions:
    def pedal_help():
        """Print out the pedal info"""
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".py")
        
        try:
            for func in functions:
                with open(temp_file.name, 'a') as sys.stdout:
                    actions.find(func, inactive=False)

            temp_file_name = temp_file.name
        finally:
            temp_file.close() 

        actions.key(OPEN_TERMINAL := "ctrl-alt-t")
        time.sleep(5)
        actions.insert(f'bat {temp_file_name}\n')

