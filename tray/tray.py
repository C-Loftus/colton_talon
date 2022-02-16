from os import getpid
from socket import socket
from talon import Module

mod = Module()

@mod.action_class
class ClientSocket:
    # ephmeral port
    def socket_send(message: str = ""):    
        '''
        send a message to the socket
        '''
        # This can be changed to a different port.
        # Just make sure it's on its own line
        # Since this is read as plaintext from the other
        # indicator.ignore-py file and not imported
        # This is since you are using two different
        #  python interpreters
        PORT = 49250
    
        s = socket()
        try:
            s.connect(('localhost', PORT))
            pid = getpid()
            msg = str(pid) + ":" + message
            s.send(msg.encode())
        except ConnectionRefusedError:
            print("program error, couldn't connect to socket")
        s.close()


        

