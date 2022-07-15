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


            savePath=Settings.UPLOAD_PATH
            if not os.path.exists(savePath):
                os.makedirs(savePath)
            file_size = os.path.getsize(savePath + "/" + file_name)
            print(f"\n[INFO] Tamaño del archivo: {file_size}")
            socket.reply(address, file_size)
            message,address= socket.receive()
            print(f"\n[INFO] Recibido: {message} desde {address}")
            

            try:
                with open(Settings.UPLOAD_PATH + "/" + file_name, mode='rb') as file:
                    remainingSize = file_size
                    while remainingSize > 0:
                        if remainingSize > self.buffer:
                            socket.receive()
                            data = file.read(self.buffer)
                            socket.reply(address, data)
                            remainingSize -= self.buffer
                        else:
                            socket.receive()
                            data = file.read(remainingSize)
                            socket.reply(address, data)
                            remainingSize = 0
                print(f"\n\n[INFO] Archivo {file_name} enviado")
            except:
                pass
                