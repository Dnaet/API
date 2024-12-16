from servicios.servicio_album import obtener_album_por_id,obtener_albunes
from servicios.servicio_photo import obtener_photo_por_id,obtener_photo
from datos.conexion_db import crear_tablas, limpiar_tablas, guardar_album, guardar_photo


albums_obtenidos=[]  #creo las listas 
photos_obtenidas=[]

def main():
    
    crear_tablas() #crea y consulta si es que existen ya las tablas
    limpiar_tablas() #para que la id no aumente cuando guarde en la bd

    while True:
        print("Menú Principal:")
        print("1. Obtener álbumes")
        print("2. Buscar un álbum por ID")
        print("3. Obtener fotos")
        print("4. Buscar una foto por ID")
        print("5. Salir con guardar en BD")
        print("6. Salir sin guardar")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            album=obtener_albunes() #guarda la lista en album
            albums_obtenidos.extend(album) # con .extender funciona /buscar
            
            
            
        
        elif opcion == "2":
            album_id = int(input("Ingrese la ID del álbum que desea buscar: "))
            obtener_album_por_id(album_id)  # llama a la funcion con id
            
            
            
        elif opcion == "3":
            photo=obtener_photo()  # guarda la lista de objetos en photo
            photos_obtenidas.extend(photo) # con .extender funciona /buscar 
            
            
            
        elif opcion == "4":
            photo_id = int(input("Ingrese la ID de la foto que desea buscar: "))
            obtener_photo_por_id(photo_id) # Llamamos a la función para buscar una foto por ID
            
            
            
        elif opcion == "5":
            if albums_obtenidos:   #...
                print(f"Guardando {len(albums_obtenidos)} álbumes...")
                for album in albums_obtenidos:
                    guardar_album(album)  # guardar los álbumes en bd
            if photos_obtenidas:
                print(f"Guardando {len(photos_obtenidas)} fotos...")
                for photo in photos_obtenidas:
                    guardar_photo(photo)  # guarda las fotos en bd
            print("Datos guardados con éxito.")
            break
        
        
        
        elif opcion == "6":
            print("Saliendo del sistema.")
            limpiar_tablas()  # limpia las tablas de datos antes de salir
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()

