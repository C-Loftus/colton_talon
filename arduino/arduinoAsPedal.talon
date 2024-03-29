# Teensy joystick library uses direct input on windows and must be
# converted to xinput with the XOutput app

# asPedal tags makes arduino call the same functions as my
# foot pedal and thus can share state and contextual overloads
tag: user.asPedal
not title: /Excel/i

-

gamepad(south:down):
    user.pedal_down('left')
gamepad(south:up):
    user.pedal_up('left')

gamepad(east:down):
    user.pedal_down('center')
gamepad(east:up):
    user.pedal_up('center')

# gamepad(west:down):
# user.pedal_down('right')

gamepad(west:up):
    # user.pedal_up('right')
    key(alt-;)

toggle arduino as pedal:
    user.toggleAsPedal()

# gamepad(d_pad_up:down):
#     print('d_pad_up')
# gamepad(d_pad_up:up):
#     print('d_pad_up')
