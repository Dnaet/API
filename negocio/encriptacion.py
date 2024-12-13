from cryptography.fernet import Fernet
import json

class Encriptador:
    def __init__(self):
        self.clave = Fernet.generate_key()
        self.cifrador = Fernet(self.clave)

    def encriptar(self, texto_claro):
        texto_bytes = texto_claro.encode()
        return self.cifrador.encrypt(texto_bytes).decode()

    def desencriptar(self, texto_cifrado):
        texto_bytes = texto_cifrado.encode()
        return self.cifrador.decrypt(texto_bytes).decode()

    def guardar_cache(self, texto_claro, texto_cifrado):
        datos = {
            "clave": self.clave.decode(),
            "texto_claro": texto_claro,
            "texto_cifrado": texto_cifrado
        }
        with open("cache.json", "w") as archivo:
            json.dump(datos, archivo)

    def cargar_cache(self):
        with open("cache.json", "r") as archivo:
            datos = json.load(archivo)
        self.clave = datos["clave"].encode()
        self.cifrador = Fernet(self.clave)
        return datos["texto_claro"], datos["texto_cifrado"]
