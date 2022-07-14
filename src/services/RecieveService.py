import os
import socket
import time
from src.config.Settings import Settings
from src.tools.RUDP import RUDPServer, RUDPClient

class RecieveService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR

    # Cliente UDP
    def startClient(self):
        print(f"\n[INFO] Intentando conexion en {self.ip}:{self.port}")
        self.recieveData()

    #Recieve data from SendService with UDP protocol
    def recieveData(self):
        socket= RUDPClient(hostname=self.ip, port=self.port)
        while True:
            try:
                reply=socket.send_recv(b'Hello')
                print(reply)
            except:
                print("Error")
                break
            time.sleep(1)
        




#todo Implementar aca todo lo que sea del servidor, no crear RecieveService
