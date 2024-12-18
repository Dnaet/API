import mysql.connector
from mysql.connector import Error
from auxiliares.constante import HOST,USER,PASSWORD,DATABASE 

def generar_conexion():
    
    #consulta conexion
    try:
        conexion = mysql.connector.connect(
            host =          HOST,       # no olvidar tiene que ser localhost
            user =          USER,            # ..
            password=       PASSWORD,            # tengo que hacer esto
            database=       DATABASE          # nombre de la base de datos
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
        return None

def crear_tablas():
    
    #las crea en BD
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            
            with open ('DDL_DATA.api.sql','r') as file:
                sql_tablas = file.read()
            
            cursor.execute(sql_tablas)  # crea las tablas

            #solo comprueba
            conexion.commit()
            print("Tablas creadas o ya existentes verificadas.") 
        except Error as e:
            print(f"Error al crear las tablas: {e}")
        finally:
            cursor.close()
            conexion.close()



def guardar_album(album):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            # INSERT
            query = "INSERT INTO albums (user_id, album_id, title) VALUES (%s, %s, %s)"
            cursor.execute(query, (album.user_id, album.album_id, album.title))
            
            # confirmar por pantalla
            conexion.commit()
            print(f"Álbum '{album.title}' guardado en la base de datos.")
        except Error as e:
            print(f"Error al guardar el álbum: {e}")
        finally:
            cursor.close()
            conexion.close()


def guardar_photo(photo):
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            # INSERT
            query = "INSERT INTO photos (album_id, photo_id, title, url, thumbnail_url) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(query, (photo.album_id, photo.photo_id, photo.title, photo.url, photo.thumbnail_url))
            
            # confirmar por pantalla
            conexion.commit()
            print(f"Foto '{photo.title}' guardada en la base de datos.")
        except Error as e:
            print(f"Error al guardar la foto: {e}")
        finally:
            cursor.close()
            conexion.close()

#Test para limpiar 
def limpiar_tablas():
  
    conexion = generar_conexion()
    if conexion:
        cursor = conexion.cursor()
        try:
            #DELETE
            cursor.execute("DELETE FROM albums")  # Elimina todos los datos de la tabla 'albums'
            cursor.execute("DELETE FROM photos")  # Elimina todos los datos de la tabla 'photos'
            
            # reinicia el contador para que la id no aumente para que la consulta no la confunda
            cursor.execute("ALTER TABLE albums AUTO_INCREMENT = 1")  
            cursor.execute("ALTER TABLE photos AUTO_INCREMENT = 1")  
            
            
            conexion.commit()  # OK
            print("Datos de las tablas 'albums' y 'photos' eliminados y contadores reiniciados.")
        except Error as e:
            print(f"Error al limpiar las tablas: {e}")
        finally:
            cursor.close()
            conexion.close()
