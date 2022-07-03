import base64
import os
import socket
from src.config.Settings import Settings

class SendService:
    ip = Settings.IP
    port = Settings.PORT
    addr = Settings.ADDR
    buffer = Settings.BUFFER_SIZE

    # Servidor UDP
    def startServer(self):
        print(f"\n[INFO] Iniciando servidor en {self.ip}:{self.port}")

        server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        server.bind((self.ip, self.port))
        
        # Send client list of all files in ../download folder and wait for response
        while True:
            data, addr = server.recvfrom(self.buffer)
            data = base64.b64decode(data)
            print(f"[INFO] Recibido: {data.decode()}")
            if data.decode() == "list":
                print(f"\n[INFO] Listando archivos en {os.getcwd()}/download")
                list = os.listdir(os.path.join(os.getcwd(), "download"))
                server.sendto(base64.b64encode(str(list).encode()), addr)

            # Se podria hacer para que posterior a mandar la lista de archivos,
            # cliente responde con cual quiere, y se envia ese archivo
            print(f"[INFO] Recibido: {data.decode()}")
            server.sendto(base64.b64encode(str("OK").encode()), addr)






        print(f"[INFO] Datos enviados")
        server.close()
        # file.close()




