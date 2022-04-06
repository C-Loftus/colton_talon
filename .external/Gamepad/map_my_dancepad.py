
from __future__ import print_function


from . import inputs

'''
TODO:  check to see if this can be automated in some way
  doesn't seem like it can be since the os doesn't know 
 anything about the visual styling of the buttons
 which is how the user interacts with it  and how mappings are made
'''
def main():
    while 1:
        events = get_gamepad()
        for event in events:
            if event.ev_type == "Key" and event.state == 1:
                message = f'You pressed key:\"{event.code}\"'
                print(message)


if __name__ == "__main__":
    main()
