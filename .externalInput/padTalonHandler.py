from talon import  fs
from pathlib import Path
#  all files we create are created in the monitor directory
#  this directory contains python files we want our own version of python to run,
#  not talon's interpreter

ROOT_DIR = "/tmp/talon_"

def on_press_left(path , flags):
    print('left')

def on_press_right(path , flags):
    print("right")

def on_press_center(path , flags):
    print('center')


fs.watch(ROOT_DIR+"center.txt", on_press_center)
fs.watch(ROOT_DIR+"left.txt", on_press_left)
fs.watch(ROOT_DIR+"right.txt", on_press_right)


