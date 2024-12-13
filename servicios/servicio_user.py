import requests
from auxiliares.urls import URL_USERS

class ServicioUser:
    def obtener_usuarios(self):
        try:
            respuesta = requests.get(URL_USERS)
            respuesta.raise_for_status()
            return respuesta.json()
        except requests.exceptions.RequestException as e:
            print(f"Error al obtener usuarios: {e}")
            return []

    def enviar_usuario(self, data):
        try:
            respuesta = requests.post(URL_USERS, json=data)
            respuesta.raise_for_status()
            if respuesta.status_code == 201:
                return "Usuario enviado correctamente."
        except requests.exceptions.RequestException as e:
            print(f"Error al enviar usuario: {e}")
            return None
