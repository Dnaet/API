from modelos.album import Album

class Photo(Album):
    def __init__(self, photo_id, album_id=0, title=None, url=None, thumbnail_url=None):
        
        super().__init__(album_id)  #cambio
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __repr__(self):  #mas facil leer el objeto con la depuraion
        return f"Photo(id={self.photo_id}, title={self.title}, album_id={self.album_id})"