from datos.conexion_db import generar_conexion
from mysql.connector import Error


#CRUD

def crear_photo(photo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "INSERT INTO photos (album_id, photo_id, title, url, thumbnail_url) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (photo.album_id, photo.photo_id, photo.title, photo.url, photo.thumbnail_url))
            conexion.commit()
            print(f"Foto '{photo.title}' creada con éxito.")
        except Error as e:
            print(f"Error al crear la foto: {e}")
        finally:
            cursor.close()
            conexion.close()
            
def leer_photos():
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            query = "SELECT * FROM photos"
            cursor.execute(query)
            photos = cursor.fetchall()
            return photos
        except Error as e:
            print(f"Error al leer las fotos: {e}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_photo(photo_id, nuevo_titulo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "UPDATE photos SET title = %s WHERE photo_id = %s"
            cursor.execute(query, (nuevo_titulo, photo_id))
            conexion.commit()
            print(f"Foto con ID {photo_id} actualizada con éxito.")
        except Error as e:
            print(f"Error al actualizar la foto: {e}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_photo(photo_id):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM photos WHERE photo_id = %s"
            cursor.execute(query, (photo_id,))
            conexion.commit()
            print(f"Foto con ID {photo_id} eliminada con éxito.")
        except Error as e:
            print(f"Error al eliminar la foto: {e}")
        finally:
            cursor.close()
            conexion.close()