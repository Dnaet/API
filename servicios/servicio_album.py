from auxiliares.constante import  ALBUMS_ENDPOINT
from servicios.servicio_url import respuesta_api
from modelos.album import Album  # importante para eva //clases//
import requests

albums_list = []

#GET

def obtener_albunes_get():
    
    url=(ALBUMS_ENDPOINT)
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

def consulta_album_por_id(album_id):
  
    # busqueda por id en la lista
    global albums_list
    album = next((album for album in albums_list if album.album_id == album_id), None)

    if album:
        print(f"Álbum encontrado: {album}")
    else:
        print(f"No se encontró un álbum con el ID {album_id}.")
    
    return album


#POST

def crear_album_post(album):
    
    try:
        url = ALBUMS_ENDPOINT  
        
        data = {
            "userId": album.user_id,
            "title": album.title
        }
        # Realizar la solicitud POST
        response = requests.post(url, json=data)

        # Validar la respuesta
        if response.status_code == 201:  # Código 201: Recurso creado
            print(f"Álbum creado exitosamente: {response.json()}")
            return response.json()  # Devuelve la respuesta JSON
        else:
            print(f"Error al crear el álbum: {response.status_code} - {response.reason}")
    except requests.RequestException as e:
        print(f"Excepción al realizar la solicitud POST: {e}")