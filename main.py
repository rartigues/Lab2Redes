import sys
from src.services.ServerService import ServerService
from src.services.ClientService import ClientService

def main():
    if(len(sys.argv)>2):
        print("[ERROR] El numero de argumentos es incorrecto.")
        sys.exit()
    elif(len(sys.argv)<2):
        print("[ERROR] No se ha ingresado ningun argumento.")
        sys.exit()
    elif(len(sys.argv)==2):
        if(sys.argv[1]=="-s" or sys.argv[1]=="--server"):
            ServerService().startServer()
        elif(sys.argv[1]=="-c" or sys.argv[1]=="--client"):
            ClientService().startClient()
        else:
            print("[ERROR] Argumento incorrecto.")
            sys.exit()
    return


if __name__ == "__main__":
    main()