import requests

class ServicioAlbum:
    API_URL = f"URL_BASE/albums"

    def obtener_albums():
        response = requests.get(ServicioAlbum.API_URL)
        if response.status_code == 200:
            return response.json()  # Devuelve los datos como una lista de diccionarios.
        else:
            raise Exception("Error al obtener los álbumes desde la API.")
