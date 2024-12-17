from servicios.servicio_album import obtener_albunes_get,crear_album_post
from servicios.servicio_photo import obtener_photo_get,crear_photo_post
from datos.conexion_db import limpiar_tablas, guardar_album, guardar_photo
from datos.data_album import leer_albums,actualizar_album,eliminar_album
from datos.data_photo import leer_photos,actualizar_photo,eliminar_photo
from modelos.album import Album
from modelos.photo import Photo
import os
from negocio.negocio_contraseña import guardar_clave_encriptada,verificar_clave

albums_obtenidos=[]  #creo las listas 
photos_obtenidas=[]


ARCHIVO_CONTRASENA="datos/clave.bin"  

def menu_principal():
    
    
    #verifica contraseña si existe el archivo
    
    if not os.path.exists(ARCHIVO_CONTRASENA):
        guardar_clave_encriptada()
    
    if not verificar_clave():
        print ("Acceso denegado. Saliendo del programa")
        return
    
    
    
    
    
    
    
    while True:
        print("Menú Principal:")
        print("1. Gestionar CRUD de Photo y Album")
        print("2. Interactuar con la API (GET y POST)")
        print("3. Borrar datos en BD")
        print("4. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            menu_crud()
        elif opcion == "2":
            menu_api()
        elif opcion == "3":
            limpiar_tablas()   
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")



def menu_crud():
    while True:
        print("\nMenú CRUD:")
        print("1. Crear álbum")
        print("2. Leer álbumes")
        print("3. Actualizar álbum")
        print("4. Eliminar álbum")
        print("5. Crear foto")
        print("6. Leer fotos")
        print("7. Actualizar foto")
        print("8. Eliminar foto")
        print("9. Volver al Menú Principal")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            user_id = int(input("Ingrese el user_id: "))
            album_id = int(input("Ingrese el album_id: "))
            title = input("Ingrese el título: ")
            album = Album(user_id, album_id, title)
            guardar_album(album)
        elif opcion == "2":
            albums = leer_albums()
            for album in albums:
                print(album)
        elif opcion == "3":
            album_id = int(input("Ingrese el album_id a actualizar: "))
            nuevo_titulo = input("Ingrese el nuevo título: ")
            actualizar_album(album_id, nuevo_titulo)
        elif opcion == "4":
            album_id = int(input("Ingrese el album_id a eliminar: "))
            eliminar_album(album_id)
        elif opcion == "5":
            album_id = int(input("Ingrese el album_id: "))
            photo_id = int(input("Ingrese el photo_id: "))
            title = input("Ingrese el título: ")
            url = input("Ingrese el URL: ")
            thumbnail_url = input("Ingrese el thumbnail URL: ")
            photo = Photo(album_id, photo_id, title, url, thumbnail_url)
            guardar_photo(photo)
        elif opcion == "6":
            photos = leer_photos()
            for photo in photos:
                print(photo)
        elif opcion == "7":
            photo_id = int(input("Ingrese el photo_id a actualizar: "))
            nuevo_titulo = input("Ingrese el nuevo título: ")
            actualizar_photo(photo_id, nuevo_titulo)
        elif opcion == "8":
            photo_id = int(input("Ingrese el photo_id a eliminar: "))
            eliminar_photo(photo_id)
        elif opcion == "9":
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida.")


def menu_api():
    while True:
        print("\nMenú API:")
        print("1. Obtener álbumes (GET)")
        print("2. Obtener fotos (GET)")
        print("3. Crear un nuevo álbum (POST)")
        print("4. Crear una nueva foto (POST)")
        print("5. Volver al Menú Principal")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            albums = obtener_albunes_get()
            albums_obtenidos.extend(albums)  # guardar en la lista en memoria
            print(f"{len(albums)} álbumes obtenidos.")
            if albums_obtenidos:   #...
                print(f"Guardando {len(albums_obtenidos)} álbumes...")
                for albums in albums_obtenidos:
                    guardar_album(albums)  # guardar los álbumes en bd
        elif opcion == "2":
            photos = obtener_photo_get()
            photos_obtenidas.extend(photos)  # guardar en la lista en memoria
            print(f"{len(photos)} fotos obtenidas.")
            if photos_obtenidas:
                print(f"Guardando {len(photos_obtenidas)} fotos...")
                for photo in photos_obtenidas:
                    guardar_photo(photos)  # guarda las fotos en bd
        elif opcion == "3":
            user_id = int(input("Ingrese el user_id: "))
            title = input("Ingrese el título del álbum: ")
            nuevo_album = Album(user_id, None, title)
            response = crear_album_post(nuevo_album)
            if response:
                print(f"Álbum creado en la API: {response}")
        elif opcion == "4":
            album_id = int(input("Ingrese el album_id: "))
            title = input("Ingrese el título de la foto: ")
            url = input("Ingrese el URL de la foto: ")
            thumbnail_url = input("Ingrese el thumbnail URL: ")
            nueva_photo = Photo(album_id, None, title, url, thumbnail_url)
            response = crear_photo_post(nueva_photo)
            if response:
                print(f"Foto creada en la API: {response}")
        elif opcion == "5":
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()

































#:DS