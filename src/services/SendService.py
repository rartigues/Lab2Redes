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
            print(f"\n[INFO] Recibido: {message} desde {address}")
            list_files = os.listdir(Settings.UPLOAD_PATH)
            socket.reply(address, list_files)


            file_name, address = socket.receive()
            print(f"\n[INFO] Recibido: {file_name} desde {address}")
            file_size = os.path.getsize(Settings.UPLOAD_PATH + "/" + file_name)
            print(f"\n[INFO] Tamaño del archivo: {file_size}")
            socket.reply(address, file_size)
            message,address= socket.receive()
            #send file to client
            print(f"\n[INFO] Recibido: {message} desde {address}")
            

            with open(Settings.UPLOAD_PATH + "/" + file_name, mode='rb') as file: # b is important -> binary
                fileContent = file.read(self.buffer)
                socket.reply(address, fileContent)             

            

