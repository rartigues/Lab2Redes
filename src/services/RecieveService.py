import os
import socket
from src.config.Settings import Settings

class RecieveService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR

    # Cliente UDP
    def startClient(self):
        print(f"\n[INFO] Intentando conexion en {self.ip}:{self.port}")

    #Recieve data from SendService with UDP protocol
    def recieveData(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.bind((self.ip, self.port))
            data, addr = sock.recvfrom(1024)
            print(f"[INFO] Recibido: {data.decode('utf-8')}")
            sock.close()
            return data.decode('utf-8')
        except Exception as e:
            print(f"[ERROR] {e}")
            return None





#todo Implementar aca todo lo que sea del servidor, no crear RecieveService
