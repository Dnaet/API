from auxiliares.constante import PHOTOS_ENDPOINT
from servicios.servicio_url import respuesta_api
from modelos.photo import Photo  # Importa la clase Photo


photos_list = []

def obtener_photo():

    url=PHOTOS_ENDPOINT
    
    photo_data = respuesta_api(url)
    
    # guardo en lista
    global photos_list
    photos_list = [Photo(photo['albumId'], photo['id'], photo['title'], photo['url'], photo['thumbnailUrl']) for photo in photo_data]

    print(f"Fotos obtenidas: {photos_list[:5]}...")  
    return photos_list












def obtener_photo_por_id(photo_id):

    # buqueda por id en la lista
    global photos_list
    photo = next((photo for photo in photos_list if photo.photo_id == photo_id), None)

    if photo:
        print(f"Foto encontrada: {photo}")
    else:
        print(f"No se encontró una foto con el ID {photo_id}.")
    
    return photo
