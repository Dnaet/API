from negocio.negocio_user import NegocioUser
from negocio.encriptacion import Encriptador
import datos.api_cliente as obtener_usuarios

def encriptar_contraseña():
    password = input("Introduce la contraseña a encriptar: ")
    encriptador = Encriptador()
    password_encriptada = encriptador.encriptar(password)
    print(f"Contraseña encriptada: {password_encriptada}")
    password_desencriptada = encriptador.desencriptar(password_encriptada)
    print(f"Contraseña desencriptada: {password_desencriptada}")
    print("Contraseña original y desencriptada coinciden." if password == password_desencriptada else "Error al comparar.")


def enviar_usuario():
    datos_usuario = {
        "name": input("Nombre: "),
        "username": input("Nombre de usuario: "),
        "email": input("Email: "),
        "phone": input("Teléfono: "),
        "website": input("Website: ")
    }
    negocio = NegocioUser()
    resultado = negocio.enviar_usuario(datos_usuario)
    print(resultado)

def mostrar_menu():
    print("1. Encriptar Contraseña")
    print("2. Obtener Usuarios desde la API")
    print("3. Enviar Usuario a la API")
    print("4. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            encriptar_contraseña()
        elif opcion == "2":
            obtener_usuarios()
        elif opcion == "3":
            enviar_usuario()
        elif opcion == "4":
            print("Saliendo del sistema.")
            break
        else:
            print("Opción inválida, intenta nuevamente.")

main()



"""
from negocio.negocio_album import NegocioAlbum
from negocio.negocio_photo import NegocioPhoto

def main():
    print("Bienvenido al sistema de gestión de datos desde la API")
    print("1. Procesar álbumes")
    print("2. Procesar fotos")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        negocio_album = NegocioAlbum()
        negocio_album.procesar_albums()
        print("Álbumes procesados e insertados en la base de datos.")
    elif opcion == "2":
        negocio_photo = NegocioPhoto()
        negocio_photo.procesar_photos()
        print("Fotos procesadas e insertadas en la base de datos.")
    else:
        print("Opción no válida.")

if __name__ == "__main__":
    main()
"""