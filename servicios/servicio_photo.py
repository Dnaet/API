import requests
from auxiliares.urls import PHOTOS_ENDPOINT

class ServicioPhoto:
    def obtener_photos():
        response = requests.get(PHOTOS_ENDPOINT)
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception("Error al obtener fotos.")
