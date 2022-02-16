# COMMENTED OUT TO NOT CONFLICT WITH KNAUSJ 
# COPY THIS INTO YOUR OWN 
# ~/.talon/user/knausj_talon/modes/modes.talon
# TO MAKE IT SO THE SOCKETS SEND MODE SWITCHES

# not mode: sleep
# -
# ^dictation mode$:
#     mode.disable("sleep")
#     mode.disable("command")
#     mode.enable("dictation")
#     user.code_clear_language_mode()
#     mode.disable("user.gdb")

#     user.socket_send("dictation")

# ^command mode$:
#     mode.disable("sleep")
#     mode.disable("dictation")
#     mode.enable("command")
    
#     user.socket_send("command")


# ^mixed mode$:
#     mode.disable("sleep")
#     mode.enable("dictation")
#     mode.enable("command")
      
#     user.socket_send("mixed")
