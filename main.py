import sys
from services.SendService import SendService
from services.RecieveService import RecieveService

def main():
    if(len(sys.argv)>2):
        print("[ERROR] El numero de argumentos es incorrecto.")
        sys.exit()
    elif(len(sys.argv)<2):
        print("[ERROR] No se ha ingresado ningun argumento.")
        sys.exit()
    elif(len(sys.argv)==2):
        if(sys.argv[1]=="-s" or sys.argv[1]=="--send"):
            SendService().startServer()
        elif(sys.argv[1]=="-r" or sys.argv[1]=="--recieve"):
            RecieveService().startClient()
        else:
            print("[ERROR] Argumento incorrecto.")
            sys.exit()
    return

if __name__ == "__main__":
    main()