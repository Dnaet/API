class Album:
    def __init__(self, user_id, album_id, title):
        self.user_id = user_id
        self.album_id = album_id
        self.title = title

    def __repr__(self): #mas facil leer el objeto con la depuraion
        return f"Album(id={self.album_id}, title={self.title}, user_id={self.user_id})"
