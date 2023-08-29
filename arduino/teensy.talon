tag: user.share_pedal_map

-

gamepad(north:down):             
    user.pedal_down('left') 
gamepad(north:up):              
    user.pedal_down('left') 

gamepad(west:down):
    user.pedal_down('right')
gamepad(west:up):
    user.pedal_up('right')

gamepad(east:down):              
    user.pedal_down('right')
gamepad(east:up):
    user.pedal_up('right')

gamepad(south:down):             
    user.pedal_down('center')
gamepad(south:up):
    user.pedal_up('center')


gamepad(d_pad_up:down):             
    print('d_pad_up')
gamepad(d_pad_up:up):
    print('d_pad_up')
