class Photo:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self.album_id = album_id
        self.photo_id = photo_id
        self.title = title
        self.url = url
        self.thumbnail_url = thumbnail_url

    def __repr__(self):  #mas facil leer el objeto con la depuraion
        return f"Photo(id={self.photo_id}, title={self.title}, album_id={self.album_id})"
