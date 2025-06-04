from Helpers.ConsultMain import consultMain
from Repositories.ArchiveUtil import ArchiveUtil
from Composables.storeMain import storeMain
import os

def Main():
    sep = os.path.sep
    actualRoute = os.path.dirname(os.path.abspath(__file__))
    storageRoute = sep.join(actualRoute.split(sep)[:-1])+sep+"Storage"

    try:
        archive = ArchiveUtil(storageRoute)
    except(NotADirectoryError, FileNotFoundError) as e:
        print("Error, al abrir el archivo: "+e)
        return

    arFinal, serialRead = consultMain(archive)

    storeMain(archive, arFinal, serialRead)

# Llamada a la funcion 
Main()