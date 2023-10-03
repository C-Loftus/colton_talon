not app.name: ITGmania
-
# Left button (numlk)
key(numlock:down):    
    user.pedal_down('left') 
key(numlock:up):       
    user.pedal_up('left') 

# Center button (kpplus)
key(keypad_divide:down):    
   user.pedal_down('center')
key(keypad_divide:up):     
    user.pedal_up('center')


# Right button (kpmult)
key(keypad_multiply:down):
    user.pedal_down('right')
key(keypad_multiply:up):  
    user.pedal_up('right') 

key(keypad_minus:up):
    user.notify('minus')

# ASCII Keyboard Codes for Arduino or Custom Pedals3
# https://www.arduino.cc/reference/en/language/functions/usb/keyboard/keyboardmodifiers/
# KEY_NUM_LOCK 0xDB 219
# KEY_KP_SLASH: 0xDC 220
# KEY_KP_ASTERISK: 0xDD 221
# KEY_KP_MINUS 0xDE 222

(pedal | pettle | paddle) help:
    user.pedal_help()
