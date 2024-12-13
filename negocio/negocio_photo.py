from servicios.servicio_photo import ServicioPhoto
from datos.data_photo import DataPhoto
from modelos.photo import Photo

class NegocioPhoto:
    def procesar_photos(self):
        photos = ServicioPhoto.obtener_photos()
        data_photo = DataPhoto()
        for photo in photos:
            photo_obj = Photo(photo['id'], photo['title'], photo['url'], photo['thumbnailUrl'], photo['albumId'])
            data_photo.insert_photo(photo_obj)
