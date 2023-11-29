# enable whisper:
#     user.mouse_helper_move_image_relative("2023-10-05_10.56.29.118961.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.5)
#     user.mouse_helper_move_image_relative("2023-10-05_10.44.38.884779.png", 0)
#     sleep(0.5)
#     mouse_click(0)
#     sleep(0.55)
#     user.mouse_helper_move_image_relative("2023-10-05_10.48.57.905941.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.05)
#     user.notify("Whisper enabled")
#     user.mouse_helper_position_restore()
# enable conformer:
#     user.mouse_helper_position_save()
#     user.mouse_helper_move_image_relative("2023-10-05_10.56.29.118961.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.5)
#     user.mouse_helper_move_image_relative("2023-10-05_10.44.38.884779.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.25)
#     user.mouse_helper_move_image_relative("2023-10-05_10.48.06.901971.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.05)
#     user.notify("Conformer enabled")
#     user.mouse_helper_position_restore()
# like message:
#     user.mouse_helper_position_save()
#     user.mouse_helper_move_image_relative("2023-10-05_11.01.38.168874.png", 0)
#     sleep(0.05)
#     mouse_click(0)
#     sleep(0.05)
#     user.mouse_helper_move_image_relative("2023-10-05_11.03.28.681384.png", 0)
#     sleep(0.05)
#     sleep(0.55)
#     user.mouse_helper_position_restore()

^target comments$:
    user.mouse_helper_position_save()
    user.mouse_helper_move_image_relative("2023-11-10_12.26.25.003443.png", 0)
    sleep(0.05)
    mouse_click(0)

toggle whisper:
    user.move_to_spot("indicator")
    user.click_spot("indicator")
    sleep(1.5)
    user.move_to_spot("recognition")
    user.click_spot("recognition")
    sleep(1.5)
    user.move_to_spot("whisper")
    user.click_spot("whisper")

toggle conformer:
    user.move_to_spot("indicator")
    user.click_spot("indicator")
    sleep(1.5)
    user.move_to_spot("recognition")
    user.click_spot("recognition")
    sleep(1.5)
    user.move_to_spot("conformer")
    user.click_spot("conformer")
