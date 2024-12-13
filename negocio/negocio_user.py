from servicios.servicio_user import ServicioUser
from datos.data_user import DataUser
from modelos.user import User

class NegocioUser:
    def procesar_usuarios(self):
        servicio = ServicioUser()
        usuarios_api = servicio.obtener_usuarios()

        usuarios = []
        for usuario in usuarios_api:
            usuario_obj = User(
                id_user=usuario['id'],
                name=usuario['name'],
                username=usuario['username'],
                email=usuario['email'],
                phone=usuario['phone'],
                website=usuario['website']
            )
            usuarios.append(usuario_obj)

        data_user = DataUser()
        data_user.insertar_usuarios(usuarios)

    def enviar_usuario(self, datos_usuario):
        servicio = ServicioUser()
        resultado = servicio.enviar_usuario(datos_usuario)
        return resultado
