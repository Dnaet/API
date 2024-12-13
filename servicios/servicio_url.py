import auxiliares.constante as url_base_jsonplaceholder


def url_servicio(origen):
    #direccion = f"{url_base}{origen}"
    direccion = f"{url_base_jsonplaceholder}{origen}"
    #direccion = f"https://jsonplaceholder.typicode.com/{origen}"
    return direccion