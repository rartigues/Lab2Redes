from ast import Raise
import logging
import os
import sys
import traceback
import base64
from dotenv import load_dotenv

load_dotenv()

class Settings:
    try:
        IP = os.getenv("IP")
        PORT = int(os.getenv("PORT"))
        ADDR = (IP, PORT)
        FORMAT = "utf-8"
        if (sys.argv[1]=="-s" or sys.argv[1]=="--server"):
            SERVER_KEY = base64.b64decode(bytes(os.getenv("SERVER_KEY"), "utf-8"))
            CLIENT_KEY = None
        elif (sys.argv[1]=="-c" or sys.argv[1]=="--client"):
            CLIENT_KEY = base64.b64decode(bytes(os.getenv("CLIENT_KEY"), "utf-8"))
            SERVER_KEY = None

    except Exception as e:
        print("\n!!!!!!!!!Error: .env!!!!!!!!!")
        raise e