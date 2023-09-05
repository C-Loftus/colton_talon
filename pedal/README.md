# My Talon Pedal

This script works by doing the following

- If a pedal is pushed down, the pedal map updated with a 'True' Boolean value.
- The dictionary is then read using a cron job.
- The corresponding function is then called based on the dictionary state.
  - i.e. if the left and center pedal are held at same time, it will call `actions.user.left_center_down()`

## Synchronous vs Asynchronous calls

- Certain functions need to wait for their return value until being called again. The setting, `user.force_synchronous`, corresponds to these functions. Otherwise, by default all functions are asynchronous and you can hold the pedal down to trigger multiple actions in quick succession
  - For instance, scrolling down a page can be done asynchronously
- Synchronous calls can only be called on the pedal up and not the pedal down.
  - Synchronous calls should only be called once at a time, and the key up is a clear indicator of that, instead of pedal down which can be held

## Overrides

- Each file in this directory defines contextually scoped pedal behavior
- Define a function in a file to override the base `main-pedal.py`
- You can also contextually set `user.pedal_scroll_amount` to contextually set how much the pedal will scroll up/down every second it is held down
- Copy the code in `.template.py` and change the functions you want to create new pedal scopes
