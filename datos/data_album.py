from datos.conexion_db import generar_conexion
from mysql.connector import Error

#CRUD



def crear_album(album):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "INSERT INTO albums (user_id, album_id, title) VALUES (%s, %s, %s)"
            cursor.execute(query, (album.user_id, album.album_id, album.title))
            conexion.commit()
            print(f"Álbum '{album.title}' creado con éxito.")
        except Error as e:
            print(f"Error al crear el álbum: {e}")
        finally:
            cursor.close()
            conexion.close()

def leer_albums():
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor(dictionary=True)
        try:
            query = "SELECT * FROM albums"
            cursor.execute(query)
            albums = cursor.fetchall()
            return albums
        except Error as e:
            print(f"Error al leer los álbumes: {e}")
        finally:
            cursor.close()
            conexion.close()

def actualizar_album(album_id, nuevo_titulo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "UPDATE albums SET title = %s WHERE album_id = %s"
            cursor.execute(query, (nuevo_titulo, album_id))
            conexion.commit()
            print(f"Álbum con ID {album_id} actualizado con éxito.")
        except Error as e:
            print(f"Error al actualizar el álbum: {e}")
        finally:
            cursor.close()
            conexion.close()

def eliminar_album(album_id):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            query = "DELETE FROM albums WHERE album_id = %s"
            cursor.execute(query, (album_id,))
            conexion.commit()
            print(f"Álbum con ID {album_id} eliminado con éxito.")
        except Error as e:
            print(f"Error al eliminar el álbum: {e}")
        finally:
            cursor.close()
            conexion.close()