from __future__ import print_function

import os
import sys

from talon import ctrl, fs

from . import automation, config, inputs

# TODO check config update
# nb call python file to start the program

PRESSED = 1
RELEASED = 0
conf = config.application_config()

def on_change(path, flags):
    if flags.renamed:
        print("Config file changed: {}".format(path))
        global conf
        conf = config.application_config()

def handle_event(event, conf, gamepad) -> None:
 
    if event.ev_type == "Key":

        actions = conf.decode_step(gamepad, event.code)
        
        if event.state == PRESSED:
            for action in actions:
                automation.perform_action(action)

        elif event.state == RELEASED:
            for action in actions:
                # pyautogui.keyUp(action)
                pass

####### TODO ########
    elif event == "Sync":
        pass
    elif event == "Misc":
        pass

def main():
    
    ROOT_DIR = os.path.realpath(os.path.dirname(__file__))
    global conf

    while 1:
        try:
            events = input.get_gamepad()
            gamepad = str(input.devices.gamepads[0])
        
        except KeyboardInterrupt:
            sys.exit(0)

        except input.UnpluggedError:
            text = "No Device Found in Your Plugged in Devices: \n\n" + "\n".join(str(d) for d in input.devices)
            sys.exit(1)

        for event in events:
            handle_event(event, conf, gamepad)


if __name__ == "__main__":
    main()
