

mode:command
-



navigate explorer:
    # matches = user.mouse_helper_find_templates_relative("2022-05-23_17.26.01.390459.png 2022-05-23_17.26.01.390459.png")
    matches = user.mouse_helper_find_template_relative("2022-05-23_17.26.01.390459.png")
    user.marker_ui_show(matches)
    print("matches shown")

   
public navigate explorer:
    matches = user.mouse_helper_find_template_relative("2022-05-24_18.39.57.328874.png")
    user.marker_ui_show(matches) 
    print("matches shown")


smack <user.marker_ui_label>:
    user.mouse_helper_position_save()
    user.marker_ui_mouse_move(marker_ui_label)
    mouse_click(0)
    user.mouse_helper_position_restore()
    sleep(0.1)
    matches = user.mouse_helper_find_template_relative("2022-05-23_17.26.01.390459.png")
    # matches = user.mouse_helper_find_templates_relative("2022-05-23_17.26.01.390459.png 2022-05-23_17.26.01.390459.png")
    user.marker_ui_show(matches)