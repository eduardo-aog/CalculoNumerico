from Composables.storeArchive import storeDataNumbers
from Repositories.Logger import Logger

def storeMain(archive, arFinal, errorPerArchive, archivesNames):
    if archive is None:
        Logger.storeArchiveLog("No se puede almacenar en un archivo vacío")        
    if arFinal is None:
        Logger.storeArchiveLog("No hay datos para almacenar")

    storeDataNumbers(archive, arFinal, errorPerArchive, archivesNames)