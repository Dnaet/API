from auxiliares.constante import PHOTOS_ENDPOINT
from servicios.servicio_url import respuesta_api
from modelos.photo import Photo  # Importa la clase Photo
import requests
import json

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

#POST

def crear_photo_post(photo):
   
    try:
        url = PHOTOS_ENDPOINT  
        
        data = {
            "albumId": photo.album_id,
            "title": photo.title,
            "url": photo.url,
            "thumbnailUrl": photo.thumbnail_url
        }
       #json.dumps convierte cualquier set de datos en JSON
        response = requests.post(url, json.dumps(data.__dict__))

        # respuestas
        if response.status_code == 201:  # 201="creado"
            print(f"Foto creada exitosamente: {response.json()}")
            return response.json()  
        else:
            print(f"Error al crear la foto: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")

#PUT

def actualizar_photo(photo):
  
    try:
        url = f"{PHOTOS_ENDPOINT}/{photo.photo_id}"
        data = {
            "albumId": photo.album_id,
            "title": photo.title,
            "url": photo.url,
            "thumbnailUrl": photo.thumbnail_url
        }
        # solicitud
        #json.dumps convierte cualquier set de datos en JSON
        response = requests.put(url, json=data)
        
        #respuesta
        if response.status_code == 200:  # 200 = "OK"
            print("Foto actualizada exitosamente:")
            return response.json()
        else:
            print(f"Error al actualizar la foto: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Error en la solicitud Put: {e}")
    
#DELETE     
        
def eliminar_photo_delete(photo):

    try:
        url = f"{PHOTOS_ENDPOINT}/{photo.photo_id}"
        response = requests.delete(url)
        
        ##
        

        if response.status_code == 200:  
            print(f"Foto eliminada exitosamente.")
        else:
            print(f"Error al eliminar la foto: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Error en la solicitud DELETE: {e}")