move left:
    key(super-shift-left)

move right:
    key(super-shift-right)

mouse center:
    user.mouse_move_center_active_window()

mouse <user.running_applications>:
    user.mouse_move_center_specific_window(running_applications)

move left with mouse:
    key(super-shift-left)
    sleep(0.5)
    user.mouse_move_center_active_window()

move right with mouse:
    # user.return_to_current_app_after(1)
    key(super-shift-right)
    sleep(0.5)
    user.mouse_move_center_active_window()
