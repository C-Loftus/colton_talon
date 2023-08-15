# Left button
key(numlock:down):    
    user.pedal_down('left') 
key(numlock:up):       
    user.pedal_up('left') 

# Center button (kpplus)
key(keypad_divide:down):    
    # print("center")
   user.pedal_down('center')
key(keypad_divide:up):     
    # print("center")
    user.pedal_up('center')


# Right button (kpmult)
key(keypad_multiply:down):
    user.pedal_down('right')
key(keypad_multiply:up):  
    user.pedal_up('right') 

# KEY_NUM_LOCK 0xDB 219
# KEY_KP_SLASH: 0xDC 220
# KEY_KP_ASTERISK: 0xDD 221

key(ctrl-shift-4):
    user.pedal_help()
