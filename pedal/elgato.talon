# deck(pedal_left): user.notify("left pedal")
# deck(pedal_middle): print("middle pedal")
# deck(pedal_right): print("right pedal")

# Left button (numlk)
deck(pedal_left:down):    
    user.pedal_down('west') 
deck(pedal_left:up):       
    user.pedal_up('west') 

# Center button (kpplus)
deck(pedal_middle:down):    
   user.pedal_down('north')
deck(pedal_middle:up):     
    user.pedal_up('north')


# Right button (kpmult)
deck(pedal_right:down):
    user.pedal_down('east')
deck(pedal_right:up):  
    user.pedal_up('east') 
