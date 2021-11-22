import socket

class SocketServer:
    s = None
    port = 0

    def __init__(self, port):
        self.port = port


    def start_socket(self):
        self.s = socket.socket()
        self.s.bind(('0.0.0.0', self.port))
        self.s.listen(0)
        print(f"Socket is listening in {self.port}")


    def run_socket(self, _callback = None):
        while (True):
            c, add = self.s.accept()
            while True:
                # Receives data from the socket.
                content = c.recv(64)
                content = content.decode('Ascii')

                if _callback:
                    _callback([float(x) for x in content.split(',')])

                c.close()
                break
