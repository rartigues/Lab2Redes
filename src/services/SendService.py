import base64
import os
import socket
import time
from src.config.Settings import Settings
from .RTTService import RTTService
from src.tools.RUDP import RUDPServer, RUDPClient

class SendService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR
    buffer = Settings.BUFFER_SIZE

    

    # Servidor UDP
    def startServer(self):
        socket=RUDPServer(self.port)
        while True:
            message, address = socket.receive()
            print(f"\n[INFO] Recibido: {message}")
            print(f"\n[INFO] De: {address}")
            socket.reply(address,b"Recibido")



