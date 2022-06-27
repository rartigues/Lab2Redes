import base64
import random
import secrets
import time
import sys
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from src.services.EncryptionService import EncryptionService

class EncryptionService:
    _encryptionService = EncryptionService()
    if (_encryptionService.SERVER_KEY is not None):
        SERVER_KEY = _encryptionService.SERVER_KEY
    elif (_encryptionService.CLIENT_KEY is not None):
        CLIENT_KEY = _encryptionService.CLIENT_KEY
    else:
        print("[ERROR] No se ha ingresado ninguna llave de encriptacion. !!!!")
        sys.exit()

    def encryptAES(self, data, key):
        nonce = secrets.token_bytes(12)
        data = nonce + AESGCM(key).encrypt(nonce, data, b'')
        return data
    
    def decryptAES(self, data, key):
        data = AESGCM(key).decrypt(data[:12], data[12:], b'')
        return data
