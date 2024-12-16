import requests



def respuesta_api(url):
    try:
        respuesta = requests.get(url)
        print(respuesta)
        respuesta.raise_for_status()

        if respuesta.status_code == 200:
            data = respuesta.json()
            return data[:100] #limita a solo 100 
        else:
            raise Exception(f"Error en la solicitud: {respuesta.status_code} - {respuesta.reason}")
            
    except requests.exceptions.Timeout:
        print("Se sobrepasó el timepo de espera para la respuesta.")
        
    except requests.exceptions.ConnectionError:
        print("Hay un problema de comunicación con le servidor.")
        
    except requests.exceptions.RequestException as error: 
        print(f"Error en la solicitud: {error}")
       