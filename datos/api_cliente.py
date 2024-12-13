import auxiliares.urls as URL_BASE 
import requests


def obtener_usuarios_api():
    #direccion = url_base("users")
    direccion = URL_BASE("users")

    try:
        respuesta = requests.get(direccion)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            return respuesta.json()

    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")

    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")
    
    except requests.exceptions.RequestException as error: 
        print(f"Error en la solicitud: {error}")