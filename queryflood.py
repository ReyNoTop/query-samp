import socket
from socket import error as socket_error

class SAMPQuery:
    # IP Address and port of server
    IP_ADDRESS = ""
    PORT = 0

    # 2 MB of buffer length
    BUFFER_LENGTH = 1024 * 2

    # Socket
    s = socket

    # Pointer
    pointer = 0
    data = ""

    def __init__(self, ip, port):
        self.IP_ADDRESS = ip
        self.PORT = port

        self.connectToServer()

    def connectToServer(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        try:
            self.s.connect((self.IP_ADDRESS, self.PORT))
        except socket_error:
            print "ERROR: Connection failed."
            exit(0)

    def getBasicInfo(self):
        self.pointer = 11

        # Let's send and receive some information
        self.s.send(self.createQuery("i"))

        return server_info


    def createQuery(self, opcode):
        query = "SAMP"

        # First, second, third and fourth bytes of server IP address.
        parsed_ip = self.IP_ADDRESS.split(".")
        query += str(chr(int(parsed_ip[0])))
        query += str(chr(int(parsed_ip[1])))
        query += str(chr(int(parsed_ip[2])))
        query += str(chr(int(parsed_ip[3])))

        # First and second byte of server port.
        query += str(chr(self.PORT & 0xff)) + str(chr(self.PORT >> 8 & 0xff))

        # Query type is appended last.
        query += opcode

        return query

    def forwardByte(self, bytecount, reverse=True):
        self.pointer += bytecount
        a = self.data[self.pointer - bytecount:self.pointer]

        if reverse:
            return a[::-1]
        else:
            return a

    @staticmethod
    def hexbytes2int(_byte):
        return int('0x'+_byte.encode('hex'), 16)



if __name__ == '__main__':
    while True:
        try:
            samp = SAMPQuery("51.81.51.165", 7777)
            print samp.getBasicInfo()
            print "Paquete enviado"
        except EOFError:
                break
