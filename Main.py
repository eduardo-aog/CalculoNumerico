from Helpers.ConsultMain import consultMain
from Repositories.ArchiveUtil import ArchiveUtil
from Composables.storeMain import storeMain
import os

def Main():
    storageRoute = os.path.dirname(os.path.abspath(__file__))+os.path.sep+"Storage"

    try:
        archive = ArchiveUtil(storageRoute)
    except(NotADirectoryError, FileNotFoundError) as e:
        print(e)
        return

    arFinal, nameArchive = consultMain(archive)

    storeMain(archive, arFinal, nameArchive)

# Llamada a la funcion 
Main()