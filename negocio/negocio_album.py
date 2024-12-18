albums_list = []

def consulta_album_por_id(album_id):
  
    # busqueda por id en la lista
    try:
        album_id = int(album_id)
        
    except ValueError:
        print("El ID debe ser un nuemero entero")
        return None
        
    album = next((album for album in albums_list if album.album_id == album_id), None)

    if album:
        print(f"Álbum encontrado: {album}")
    else:
        print(f"No se encontró un álbum con el ID {album_id}.")
    
    return album