from __future__ import print_function
import os
import sys
import padLib as inputs
from pathlib import Path

PRESSED=1
RELEASED=0

def parse_key_code(action):
    """
    Parse the key code from the action string.
    """
    keyList = {
        "BTN_BASE"   : "left",
        "BTN_PINKIE" : "right",
        "BTN_TRIGGER": "center",
    }
    try:
        return keyList[action]
    except KeyError:
        return None 

def handle_event(event) -> None:
    # print(f'{event=}{type(event)=}{event.state=}{dir(event)=}')
    if event.ev_type == "Key":
        if event.state == PRESSED:
            name = parse_key_code(event.code)
            print(name)
            # Update a file with that name
            Path(f'/tmp/talon_{name}.txt').touch()

    #### TODO
        # elif event.state == RELEASED:
    # elif event == "Sync":
    #     pass
    # elif event == "Misc":
    #     pass

def main():
    
    while 1:
        try:
            events = inputs.get_gamepad()
        
        except KeyboardInterrupt:
           sys.exit(0)

        except inputs.UnpluggedError:
            text = "No Device Found in Your Plugged in Devices: \n\n" + "\n".join(str(d) for d in inputs.devices)
            print(text)
            sys.exit(1)

        for event in events:
            handle_event(event )


if __name__ == "__main__":
    main()
