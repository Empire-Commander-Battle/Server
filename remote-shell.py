#!/usr/bin/env python3
import socket
import struct
import argparse
import time

class RCONPacket(object):
    def __init__(self, ReqID=0, S1=0, ServerData=255, RecvData=255):
        self.RequestId = ReqID
        self.String1 = S1
        self.String2 = ""
        self.ServerData = ServerData
        self.RecvData = RecvData

    def OutputAsBytes(self):
        PacketSize = 4+4+len(self.String1)+1+len(self.String2)+1
        ByteArray = bytearray( struct.pack("<I", PacketSize))
        ByteArray += bytearray( struct.pack("<I", self.RequestId))
        ByteArray += bytearray( struct.pack("<I", self.ServerData))
        ByteArray += bytearray( self.String1.encode())
        ByteArray += b'\x00'
        ByteArray += bytearray(self.String2.encode())
        ByteArray += b'\x00'
        return ByteArray

class RconConnection(object):
    def __init__(self, ip, port, password, interval, timeout):
        self.ip = ip
        self.port = port
        self.socket = None
        self.interval = interval
        self.timeout = timeout
        self.password = password
        self.authenticated = False

    def connect_loop(self):
       while True:
           if self.connect():
               print('Connected.')
               return
           else:
               print(f'Connection failed retrying in {self.interval} seconds.')

           time.sleep(self.interval)

    def connect(self):
        print(f"Connecting to {self.ip}:{self.port}.")

        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.settimeout(self.timeout)

        self.authenticated = False

        try:
            self.socket.connect((self.ip,self.port))
            self.auth()
        except ConnectionRefusedError:
            print("Connection refused.")
            return False
        except TimeoutError:
            print("Timeout error.")
            return False
        except Exception as e:
            print(e)
            return False


        if not self.authenticated:
            self.close()
            print("Failed to authenticate with server.")
            return False
        return True

    #do not call
    def auth(self):
        AuthPacket = RCONPacket(1, self.password, 3)
        self.socket.send(AuthPacket.OutputAsBytes())
        self.socket.recv(1024)
        response = self.socket.recv(1024)
        val = struct.unpack('<i', response[4:8])[0]
        if val > 0:
            self.authenticated = True

    def command(self, command):
        if self.authenticated:
            packet = RCONPacket(2, command, 2)
            self.socket.send(packet.OutputAsBytes())
            run = True
            text = ""
            while run:
                response = self.socket.recv(4100)
                if len(response) < 4:
                    print("Empty response. Are you sure that server is running?.")
                    return False

                numChars = struct.unpack('<I',response[:4])[0]
                text += response[12:-2].decode()
                if numChars < 4096:
                    run = False
            return text
        else:
            print("Command '" + command + "' failed because of authentication errors.")
            return False

    def close(self):
        if self.socket is not None:
            self.socket.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(prog="warband-rcon",
                                         description="rcon shell for mount and blade warband",
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter)

        parser.add_argument("hostname", default="127.0.0.1", nargs="?")
        parser.add_argument("-p", "--port", default=7340, type=int)
        parser.add_argument("-s", "--secret", default="qwerty")
        parser.add_argument("-i", "--interval", default=5, type=int,
                            help="interval between reconnection attempts.")
        parser.add_argument("-t", "--timeout", default=2, type=int,
                            help="connection timeout.")

        args = parser.parse_args()

        with RconConnection(args.hostname, args.port, args.secret, args.interval, args.timeout) as connection:
            connection.connect_loop()

            while True:
                command = input("Input: ")

                if len(command) > 0 and command[0] == ':':
                    command = command.split()
                    match command[0]:
                        case ":reconnect":
                            connection.connect_loop()
                        case ":exit":
                                exit(0)
                        case ":help":
                            print(":exit - exits")
                            print(":reconnect - attempts to reconnect")
                            print(":help - displays this message")
                else:
                    answer = connection.command(command)
                    if answer is False:
                        connection.connect_loop()
                    else:
                        print(answer)
    except KeyboardInterrupt:
        print('')
        exit(0)
