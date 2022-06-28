import base64
import os
import socket
from src.config.Settings import Settings

class ServerService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR
    buffer = Settings.BUFFER_SIZE

    # Servidor UDP
    def startServer(self):
        print(f"\n[INFO] Iniciando servidor en {self.ip}:{self.port}")

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.ip, self.port))

        #todo Wait for connection from client, then continue
        # Como se hace para que se quede esperando?
    



        file = open(f"{os.getcwd()}/../../download/server/dogegif.gif", "r")
        data = file.read(self.buffer)

        while data:
            if(server.sendto(base64.b64encode(data), self.addr)):
                print(f"[INFO] Enviando datos...")
                data = file.read(self.buffer)
        server.sendto(base64.b64encode(b"EOF"), self.addr) #! EOF
        print(f"[INFO] Datos enviados")
        server.close()
        file.close()




