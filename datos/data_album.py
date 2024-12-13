from datos.conexion_db import get_connection

class DataAlbum:
    def insert_album(self, album):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO albums (id, title, userId) VALUES (?, ?, ?)
            """, (album.id, album.title, album.userId))
            conn.commit()

    def fetch_albums(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM albums")
            return cursor.fetchall()
