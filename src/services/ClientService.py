import os
import socket
from src.config.Settings import Settings

class ClientService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR

    # Cliente UDP
    def startClient(self):
        print(f"\n[INFO] Intentando conexion en {self.ip}:{self.port}")






#todo Implementar aca todo lo que sea del servidor, no crear RecieveService
