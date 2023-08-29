# This code is separated from my pedal and won't
# share any state or overload

# we need the as.Arduino tag since the teensy operates on presses
# but the pedal operates differently on pedal:up vs pedal:down
# These functions don't override each other, so both pedal code
# and arduino code could be called given the fact gamepad(west) and
# gamepad(west:up) are not the same command
# Thus we need a default tag for the proper override

tag: user.asArduino

-

gamepad(west):              
    print("west/X")
gamepad(east):              
    print("east/B")
gamepad(south):             
    print("south/A")
gamepad(north):             
    print("north/Y")

toggle pedal:
    user.toggleAsPedal()