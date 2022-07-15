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
        client= RUDPClient(hostname=self.ip, port=self.port)
        
        # try:

        reply=client.send_recv('Holis existo', Settings.BUFFER_SIZE)
        #this reply equals a list of different name files in the directory
        #display the list of files and ask the user to choose one
        print(f"\n[INFO] Recibido: {reply}")
        print(f"\n[INFO] Seleccione un archivo:")
        for i in range(len(reply)):
            print(f"{i} - {reply[i]}")
        file_index=int(input("\nIngrese el numero del archivo: "))
        fileName = reply[file_index]

        file_size=client.send_recv(reply[file_index], Settings.BUFFER_SIZE)
        print(f"\n[INFO] Tamaño del archivo: {file_size}")

        #recieve all the file packets
        remainingSize = file_size
        with open(Settings.DOWNLOAD_PATH + "/" + fileName, mode='wb') as file:
            while remainingSize > 0:
                if remainingSize > Settings.BUFFER_SIZE:
                    data = client.send_recv('', Settings.BUFFER_SIZE+1024*1024)
                    file.write(data)
                    remainingSize -= Settings.BUFFER_SIZE
                else:
                    data = client.send_recv('', remainingSize+1024*1024)
                    file.write(data)
                    remainingSize = 0
        print(f"\n[INFO] Archivo {fileName} recibido")
        


            # fileContent = client.send_recv('', file_size+(1024*1024))
            # file.write(fileContent)
            # print(f"\n[INFO] Archivo {fileName} recibido")


        




        # file_data=socket.send_recv('a')
        # #mirar esto depsues
        # print(f"\n[INFO] Recibido: {fileName}")
        # print(f"\n[INFO] Guardando archivo: {fileName}")
        # # save file in DOWNLOAD_PATH
        # savePath=Settings.DOWNLOAD_PATH
        # if not os.path.exists(savePath):
        #     os.makedirs(savePath)
        # with open(savePath + "/" + fileName, mode='wb') as file:
        #     file.write(file_data)
        # print(f"\n[INFO] Archivo guardado: {fileName}")
        # # except:
        # #     print("Error")
        # time.sleep(1)
        




#todo Implementar aca todo lo que sea del servidor, no crear RecieveService
