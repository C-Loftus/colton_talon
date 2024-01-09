# My Talon Pedal

## How to Use This Code Yourself

- By default the pedal code assumes your hardware is pressing the following keys: `numlock` `keypad_divide` `keypad_multiply` `keypad_minus` (These are the keys within the `main-pedal.talon` file). These keys update the state of the `north`, `west`, `east`, and `south` pedals in the map object in the Python code.
  - If your pedal can't be remapped in hardware, you can use software to remap the keys
    - Check out [https://talon.wiki/hardware/#custom-gamepads](https://talon.wiki/hardware/#custom-gamepads) for more information on ways to remap at the software level
  - If that is not possible, you can just change the keys in the `main-pedal.talon` file to whatever keys you want
    - Make sure they are keys that you don't use often, since they will be consumed by Talon and not sent to other OS applications
- Clone this repo into your Talon user directory
  - You can download the code from just this folder by using [https://download-directory.github.io/](https://download-directory.github.io/)
  - If you have the pedal configuration listed above, it should work out of the box

## Custom Behavior and Internals

**Please read this documentation before customizing**

This code works by doing the following:

- If a pedal is pushed down, the internal pedal map gets updated
- The dictionary is then read using a cron job.
- The corresponding function is then called based on the map state.
  - i.e. if the left and center pedal are pressed at same time, it will call `actions.user.left_center_down()`

## Overrides and Actions

- Each file in the `overrides` directory defines contextually scoped pedal behavior
- Define a function in a file to override the base `pedal-action-defaults.py`
- You can also contextually set `user.pedal_scroll_amount` to contextually set how much the pedal will scroll up/down every second it is held down
- Copy the code in `.template.py` and change the functions you want to create new pedal scopes
  - `.template.py` is a template and not actually used by Talon since it is prefixed with a `.`

## Repeated or Single Function Calls

- For certain functions we only want to trigger them once every time we press the pedal. ( This for instance could be an API call or some sort of remote procedure call) `user.oneActionPerPedalPress` specifies contexts with these functions. Otherwise, by default all functions can be automatically repeated and you can hold the pedal down to trigger multiple actions in quick succession
  - For instance, scrolling down a page can be done by holding the pedal down
  - However, if we are doing a Visual Studio Code RPC through a `user.vscode` command, we should block until we get a response. In this context it would be appropriate to have only one action per pedal press.
- Functions that should only be triggered once should be placed within a pedal up action. This is since we know that a pedal up action will only be triggered once per pedal press.
- On the other hand, functions that should be triggered multiple times should be placed within a pedal down action. This is since Talon will repeatedly trigger the pedal down action while the pedal is held down, even for just a short period of time.

## Holds

- Holds are a specific type of action that is only triggered after the pedal has been held down for a certain amount of seconds.
  - By default, 2 seconds is the hold time.
- Holds can only be triggered in contexts where `user.oneActionPerPedalPress` is True, otherwise, the action will just repeat and the hold won't be triggered.
  - So for instance, scrolling with the pedal has `user.oneActionPerPedalPress` set to False, so we can scroll down a page repeatedly without triggering a hold.

## Custom Hardware

- If you have an arduino and want to make a custom pedal that can use this repo's code, you can use the `fsr.ino` file in the `arduino_custom_pedal` directory
  - That arduino code is a fork of [https://github.com/teejusb/fsr/blob/master/fsr.ino](https://github.com/teejusb/fsr/blob/master/fsr.ino)-
  - For info on creating a custom pedal with Arduino see [https://www.arduino.cc/reference/en/language/functions/usb/keyboard/keyboardmodifiers/](https://www.arduino.cc/reference/en/language/functions/usb/keyboard/keyboardmodifiers/)
    - Key codes are as follows:
      - KEY_NUM_LOCK 0xDB 219
      - KEY_KP_SLASH: 0xDC 220
      - KEY_KP_ASTERISK: 0xDD 221
      - KEY_KP_MINUS 0xDE 222

## Misc

If the pedal doesn't work alongside NVDA you may need to restart NVDA
