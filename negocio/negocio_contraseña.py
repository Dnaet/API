from cryptography.fernet import Fernet
import os

ARCHIVO_CONTRASENA = "clave.bin"  

def generar_clave():
    return Fernet.generate_key()

def encriptador(clave, contraseña):
    fernet = Fernet(clave)
    contraseña_encriptada = fernet.encrypt(contraseña.encode())
    return contraseña_encriptada

def guardar_clave_encriptada():
    clave = generar_clave()
    
    # encriptar la contraseña
    contraseña = "123"  # test
    contraseña_encriptada = encriptador(clave, contraseña)

    # guardar la clave y la contraseña 
    with open(ARCHIVO_CONTRASENA, 'wb') as archivo:
        archivo.write(clave + b"\n" + contraseña_encriptada) 

    print(f"Contraseña generada y guardada encriptada: {ARCHIVO_CONTRASENA}")

def verificar_clave():
    if not os.path.exists(ARCHIVO_CONTRASENA):
        print("Archivo de contraseña no encontrado.")
        return False

   
    with open(ARCHIVO_CONTRASENA, 'rb') as archivo:
        datos = archivo.read().split(b"\n")
        clave = datos[0]  #lee lo primero
        contraseña_encriptada = datos[1]  #leer a segunda parte que si es la contraseña

    # desencripta
    fernet = Fernet(clave)
    contraseña_desencriptada = fernet.decrypt(contraseña_encriptada).decode()

    # compara
    contraseña_usuario = input("Introduce la contraseña: ")

    if contraseña_usuario == contraseña_desencriptada:
        print("Acceso concedido.")
        return True
    else:
        print("Contraseña incorrecta.")
        return False
