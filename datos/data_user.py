from datos.conexion_db import generar_conexion
from modelos.user import User

class DataUser:
    def insertar_usuarios(self, usuarios):
        consulta = """
            INSERT INTO users (id_user, name, username, email, phone, website) 
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        datos = [(usuario.id_user, usuario.name, usuario.username, usuario.email, usuario.phone, usuario.website)
                 for usuario in usuarios]

        conexion = generar_conexion()
        if conexion:
            cursor = conexion.cursor()
            cursor.executemany(consulta, datos)
            conexion.commit()
            cursor.close()
            conexion.close()
