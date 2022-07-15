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
        
        # try:

        reply=socket.send_recv(b'Holis existo')
        #this reply equals a list of different name files in the directory
        #display the list of files and ask the user to choose one
        print(f"\n[INFO] Recibido: {reply}")
        print(f"\n[INFO] Seleccione un archivo:")
        for i in range(len(reply)):
            print(f"{i} - {reply[i]}")
        file_index=int(input("\nIngrese el numero del archivo: "))
        #send the name of the file to the server


        file_size=socket.send_recv(reply[file_index])
        print(f"\n[INFO] Tamaño del archivo: {file_size}")


        file_data=socket.send_recv('a')
        #mirar esto depsues
        print(f"\n[INFO] Recibido: {file_data}")
        file_name="RobLindouwu.gif"
        print(f"\n[INFO] Guardando archivo: {file_name}")
        with open(file_name, 'wb') as f:
            f.write(file_data)
        print(f"\n[INFO] Archivo guardado: {file_name}")
        # except:
        #     print("Error")
        time.sleep(1)
        




#todo Implementar aca todo lo que sea del servidor, no crear RecieveService
