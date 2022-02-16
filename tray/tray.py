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


        

