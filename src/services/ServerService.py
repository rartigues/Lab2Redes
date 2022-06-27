import os
import socket
from src.config.Settings import Settings

class ServerService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR

    # Servidor UDP
    def startServer(self):
        print(f"\n[INFO] Iniciando servidor en {self.ip}:{self.port}")

    #todo Implementar aca todo lo que sea del servidor, no crear RecieveService
