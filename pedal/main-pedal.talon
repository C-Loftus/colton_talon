not app.name: ITGmania
-
# Left button (numlk)
key(numlock:down):
    user.pedal_down('west')
key(numlock:up):
    user.pedal_up('west')

# Center button (kpplus)
key(keypad_divide:down):
    user.pedal_down('north')
key(keypad_divide:up):
    user.pedal_up('north')

# Right button (kpmult)
key(keypad_multiply:down):
    user.pedal_down('east')

key(keypad_multiply:up):
    user.pedal_up('east')

key(keypad_minus:down):
    user.pedal_down('south')
key(keypad_minus:up):
    user.pedal_up('south')

toggle tab mode:
    user.toggle_tab_mode()

help (pedal | pettle | paddle):
    user.pedal_help()

toggle pedal actions:
    user.disable_pedal_toggle()

# Resets scroll speed, tags, etc.
reset (penal | pedal | pettle | paddle) state:
    user.reset_pedal_state()
