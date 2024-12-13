from datos.conexion_db import get_connection

class DataPhoto:
    def insert_photo(self, photo):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO photos (id, title, url, thumbnailUrl, albumId) VALUES (?, ?, ?, ?, ?)
            """, (photo.id, photo.title, photo.url, photo.thumbnailUrl, photo.albumId))
            conn.commit()

    def fetch_photos(self):
        with get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM photos")
            return cursor.fetchall()
