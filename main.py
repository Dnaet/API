from servicios.servicio_album import obtener_albunes_get,crear_album_post
from negocio.negocio_album import consulta_album_por_id
from negocio.negocio_photo import consulta_photo_por_id
from servicios.servicio_photo import obtener_photo_get,crear_photo_post
from datos.conexion_db import crear_tablas, limpiar_tablas, guardar_album, guardar_photo
from datos.data_album import crear_album,leer_albums,actualizar_album,eliminar_album
from datos.data_photo import crear_photo,leer_photos,actualizar_photo,eliminar_photo
from modelos.album import Album
from modelos.photo import Photo
import os
from negocio.negocio_contraseña import guardar_clave_encriptada,verificar_clave
from auxiliares.constante import MENU_API,MENU_CRUD,MENU_PRINCIPAL


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
    
    
    crear_tablas()
    
    
    
    
    while True:
        print("MENU PRINCICAL")
        for opcion in MENU_PRINCIPAL:
            print(opcion)

        opcion = input("Elige una opción: ")
        if opcion == "1":
            menu_BD()
        elif opcion == "2":
            menu_API()
        elif opcion == "3":
            limpiar_tablas()   
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción no válida.")



def menu_BD():
    while True:
        print("MENU BD")
        for opcion in MENU_CRUD:
            print(opcion)

        opcion = input("Elige una opción: ")
        
        
        if opcion == "1":
            user_id = int(input("Ingrese el user_id: "))
            album_id = int(input("Ingrese el album_id: "))
            title = input("Ingrese el título: ")
            album = Album(user_id, album_id, title)
            crear_album(album)
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
            crear_photo(photo)
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


def menu_API():
    while True:
        print("MENU API")
        for opcion in MENU_API:
            print(opcion)

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
                for photos in photos_obtenidas:
                    guardar_photo(photos)  # guarda las fotos en bd
        elif opcion == "3":
            
            album_id=input("ingresa album_id: ")
            consulta_album_por_id(album_id)
        elif opcion == "4":
            
            photo_id=input("ingresa photo_id: " )
            consulta_photo_por_id(photo_id)
        elif opcion == "5":
            photo_id = int(input("Ingrese el photo_id: "))
            title = input("Ingrese el título del álbum: ")
            nuevo_album = Album(photo_id, None, title)
            response = crear_album_post(nuevo_album)
            if response:
                print(f"Álbum creado en la API: {response}")
        elif opcion == "6":
            album_id = int(input("Ingrese el album_id: "))
            title = input("Ingrese el título de la foto: ")
            url = input("Ingrese el URL de la foto: ")
            thumbnail_url = input("Ingrese el thumbnail URL: ")
            nueva_photo = Photo(album_id, None, title, url, thumbnail_url)
            response = crear_photo_post(nueva_photo)
            if response:
                print(f"Foto creada en la API: {response}")
        elif opcion == "7":
            album_id = int(input("Ingrese el album_id a actualizar: "))
            title = input("Ingrese el nuevo título del álbum: ")
            response = actualizar_album(album_id, title)
            if response:
                print(f"Álbum actualizado: {response}")      
        elif opcion == "8":
            photo_id = int(input("Ingrese el photo_id a actualizar: "))
            title = input("Ingrese el nuevo título de la foto: ")
            response = actualizar_photo(photo_id, title)
            if response:
                print(f"Foto actualizada: {response}")   
        elif opcion == "9":
            album_id = int(input("Ingrese el album_id a eliminar: "))
            response = eliminar_album(album_id)
            if response:
                print(f"Álbum eliminado: {response}")
        elif opcion == "10":
            photo_id = int(input("Ingrese el photo_id a eliminar: "))
            response = eliminar_photo(photo_id)
            if response:
                print(f"Foto eliminada: {response}")
        elif opcion == "11":
            print("Volviendo al Menú Principal...")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    menu_principal()






