# My Talon Pedal

This script works by doing the following

- If a pedal is pushed down, the a pedal map gets ,updated with a 'True' Boolean value.
- The dictionary is then read using a cron job.
- The corresponding function is then called based on the dictionary state.
  - i.e. if the left and center pedal are held at same time, it will call `actions.user.left_center_down()`

## Repeated or Single Function Calls

- For certain functions we only want to trigger them once every time we press the pedal. ( This for instance could be an API call or some sort of remote procedure call) `user.oneActionPerPedalPress` specifies contexts with these functions. Otherwise, by default all functions can be automatically repeated and you can hold the pedal down to trigger multiple actions in quick succession
  - For instance, scrolling down a page can be done  by holding the pedal down
  -  However, if we are communicating with Visual Studio Code through  a `user.vscode` command,  we should block until we get a response.  In this context it would be appropriate to have only one action per pedal press.
-  Functions that should only be triggered once should be placed within a pedal up action.  This is since we know that a pedal up action will only be triggered once per pedal press. 
-   On the other hand, functions that should be triggered multiple times should be placed within a pedal down action.  This is since Talon will repeatedly trigger the pedal down action while the pedal is held down, even for just a short period of time.

## Overrides

- Each file in this directory defines contextually scoped pedal behavior
- Define a function in a file to override the base `pedal-action-defaults.py`
- You can also contextually set `user.pedal_scroll_amount` to contextually set how much the pedal will scroll up/down every second it is held down
- Copy the code in `.template.py` and change the functions you want to create new pedal scopes
