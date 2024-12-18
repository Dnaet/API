from auxiliares.constante import  ALBUMS_ENDPOINT
from servicios.servicio_url import respuesta_api
from modelos.album import Album  # importante para eva //clases//
import requests
import json

albums_list = []

#GET

def obtener_albunes_get():
    
    
    data_album=respuesta_api(ALBUMS_ENDPOINT)

    #test si recibe datos //Depurar
    if data_album is None:
        print("Error: no se obtuvieron datos de la api")
        return []
    
    if not data_album:
        print("No se obtuvieron datos de la api")
        return[]
    
    global albums_list
    albums_list = [Album(album['userId'], album['id'], album['title']) for album in data_album]
    
    
    print(f"Se obtuvieron {len(albums_list)} álbumes. Aquí un resumen de los primeros 5:")
    for album in albums_list[:5]: # Print() algunos datos para una consulta mas facil y asi pruebo que funciono
        print(album)

    return albums_list

#POST

def crear_album_post(album):
    
    try:
        url = ALBUMS_ENDPOINT 
        
        data = {
            "userId": album.user_id,
            "title": album.title
        }
                       
                        # solicitud
        
        #json.dumps convierte cualquier set de datos en JSON
        response = requests.post(url, json.dumps(data.__dict__))

        # respuesta
        if response.status_code == 201:  # 201="creado"
            print(f"Álbum creado exitosamente: {response.json()}")
            return response.json()  # Devuelve la respuesta JSON
        else:
            print(f"Error al crear el álbum: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")
             
#PUT

def actualizar_album_post(album):
    
    try:
        url = f"{ALBUMS_ENDPOINT}/{album.album_id}"
        
        data = {
            "userId": album.user_id,
            "title": album.title
        }
        # solicitud
        #json.dumps convierte cualquier set de datos en JSON
        response = requests.put(url, json.dumps(data.__dict__))

        # respuesta
        if response.status_code == 201:  # 201="creado"
            print(f"Álbum actualizado exitosamente:")
            return response.json()  # Devuelve la respuesta JSON
        else:
            print(f"Error al crear el álbum: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")    
        
#DELETE

def actualizar_album_post(album):
    
    try:
        url = f"{ALBUMS_ENDPOINT}/{album.album_id}"
         
        # solicitud
        #json.dumps convierte cualquier set de datos en JSON
        response = requests.delete(url)

        # respuesta
        if response.status_code == 200:  
            print(f"Álbum eliminado exitosamente: {response.json()}")
        else:
            print(f"Error al eliminar el álbum: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")