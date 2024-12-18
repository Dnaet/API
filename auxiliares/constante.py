from auxiliares.urls import URL_BASE as url

#  ...API


PHOTOS_ENDPOINT =   f"{url}photos"

ALBUMS_ENDPOINT =   f"{url}albums"


# ----BD


HOST = 'localhost'
USER = 'root'
PASSWORD = ''  
DATABASE = 'api'


#---------menu

MENU_PRINCIPAL = [
    "1. Gestionar CRUD de Photo y Album",
    "2. Interactuar con la API",
    "3. Borrar datos en BD",
    "4. Salir"
]


MENU_CRUD = [
    "1. Crear álbum",
    "2. Leer álbumes",
    "3. Actualizar álbum",
    "4. Eliminar álbum",
    "5. Crear foto",
    "6. Leer fotos",
    "7. Actualizar foto",
    "8. Eliminar foto",
    "9. Volver al Menú Principal"
]


MENU_API = [
    "1. Obtener álbumes(GET) ",
    "2. Obtener fotos(GET) ",
    "3. Consulta álbum por ID",
    "4. Consulta foto por ID",
    "5. Crear un nuevo álbum(POST)",
    "6. Crear una nueva foto(POST) ",
    "7. Actualiza un nuevo album(PUT) ",
    "8. Actualiza una nueva foto (PUT)",
    "9. Eliminar Un Album(DELETE)",
    "9. Eliminar Una Photo(DELETE)",
    "9. Volver al Menú Principal"
]