from auxiliares.constante import PHOTOS_ENDPOINT
from servicios.servicio_url import respuesta_api
from modelos.photo import Photo  
import requests

photos_list = []

#GET

def obtener_photo_get():

    url=PHOTOS_ENDPOINT
    
    photo_data = respuesta_api(url)
    
    # guardo en lista
    global photos_list
    photos_list = [Photo(photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']) for photo in photo_data]

    print(f"Fotos obtenidas: {photos_list[:5]}...")  
    return photos_list


def consulta_photo_por_id(photo_id):

    # buqueda por id en la lista
    global photos_list
    photo = next((photo for photo in photos_list if photo.photo_id == photo_id), None)

    if photo:
        print(f"Foto encontrada: {photo}")
    else:
        print(f"No se encontró una foto con el ID {photo_id}.")
    
    return photo

#POST

def crear_photo_post(photo):
   
    try:
        url = PHOTOS_ENDPOINT  # URL base para las fotos
        # Estructura del cuerpo de la solicitud
        data = {
            "albumId": photo.album_id,
            "title": photo.title,
            "url": photo.url,
            "thumbnailUrl": photo.thumbnail_url
        }
        # Realizar la solicitud POST
        response = requests.post(url, json=data)

        # Validar la respuesta
        if response.status_code == 201:  # Código 201: Recurso creado
            print(f"Foto creada exitosamente: {response.json()}")
            return response.json()  # Devuelve la respuesta JSON
        else:
            print(f"Error al crear la foto: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")