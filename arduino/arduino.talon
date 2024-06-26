# This code is separated from my pedal and won't
# share any state or overload
# we need the as.Arduino tag since the teensy operates on presses
# but the pedal operates differently on pedal:up vs pedal:down
# These functions don't override each other, so both pedal code
# and arduino code could be called given the fact gamepad(west) and
# gamepad(west:up) are not the same command
# Thus we need a mutually exclusive tag for the proper override
tag: user.asArduino
-

gamepad (west):
    speech.toggle()
gamepad (east):
    print("east/B")

gamepad (south):
    # user.toggleFluentSearchTags()
    user.toggle_reader()

toggle arduino as pedal:
    user.toggleAsPedal()
