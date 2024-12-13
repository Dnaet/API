import mysql.connector
from mysql.connector import errorcode

def generar_conexion():
    config = {
        'host': "127.0.0.1",
        'user': "dnaet",  
        'password': "", 
        'database': "API"  
    }
    try:
        conexion = mysql.connector.connect(**config)
        if conexion.is_connected():
            return conexion
    except mysql.connector.Error as error:
        print(f"Error al conectar a la base de datos: {error}")
    return None
