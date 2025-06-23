from Composables.storeArchive import storeData
from Repositories.Logger import storeArchiveLog

def storeMain(archive, arFinal, errorPerArchive, archivesNames):
    if archive is None:
        storeArchiveLog("No se puede almacenar en un archivo vacío")        
    if arFinal is None:
        storeArchiveLog("No hay datos para almacenar")

    storeData(archive, arFinal, errorPerArchive, archivesNames)