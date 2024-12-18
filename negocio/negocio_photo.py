

photos_list = []

def consulta_photo_por_id(photo_id):

    # buqueda por id en la lista
    
    try:
        photos_list = int(photo_id)
        
    except ValueError:
        print("El ID debe ser un nuemero entero")
        return None
   
    photo = next((photo for photo in photos_list if photo.photo_id == photo_id), None)

    if photo:
        print(f"Foto encontrada: {photo}")
    else:
        print(f"No se encontró una foto con el ID {photo_id}.")
    
    return photo