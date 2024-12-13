from servicios.servicio_album import ServicioAlbum
from datos.data_album import DataAlbum
from modelos.album import Album

class NegocioAlbum:
    def procesar_albums(self):
        albums = ServicioAlbum.obtener_albums()
        data_album = DataAlbum()
        for album in albums:
            album_obj = Album(album['id'], album['title'], album['userId'])
            data_album.insert_album(album_obj)
