from talon import Module, Context,cron, actions
import time
import sys


import tempfile
import inspect

ctx = Context()
mod = Module()




functions = [
    # actions.user.left_center_right_down.__call__,
    "user.center_right_down",
    "user.left_right_down",
    "user.left_center_down",
    "user.left_down",
    "user.right_down",
    "user.center_down",
    "user.left_up",
    "user.right_up",
    "user.center_up"
]

@mod.action_class
class UserActions:
    def pedal_help():
        """Print out the pedal info"""
        temp_file = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix=".py")
        
        try:
            for func in functions:
                with open(temp_file.name, 'a') as sys.stdout:
                    actions.find(func)

            temp_file_name = temp_file.name
        finally:
            temp_file.close()

        time.sleep(1)
        actions.key("ctrl-alt-t")
        time.sleep(5)
        actions.insert(f'bat {temp_file_name}\n')



# def pedal_held_down(key, map, seconds):

#     held_down=True

#     def check_down():
#         if not map[key]:
#             held_down=False

#     cron.interval(fd, on_interval)