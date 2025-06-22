from Composables.storeArchive import storeData

def storeMain(archive, arFinal, serialRead):
    if archive is None:
        raise ValueError("No se puede almacenar en un archivo vacío")
        
    if arFinal is None:
        raise ValueError("No hay datos para almacenar")
        
    if serialRead is None:
        raise ValueError("El nombre del archivo es inválido")

    storeData(archive, arFinal, serialRead)