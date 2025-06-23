from Helpers.ConsultMain import consultMain
from Repositories.ArchiveUtil import ArchiveUtil
from Composables.storeMain import storeMain
from Repositories.Logger import storeArchiveLog
import os

def Main():
    try:
        storageRoute = os.path.dirname(os.path.abspath(__file__))+os.path.sep+"Storage"
        archive = ArchiveUtil(storageRoute)
    except(NotADirectoryError, FileNotFoundError) as e:
        storeArchiveLog(e+"")
        exit()

    arFinal, errorPerArchive, archivesNames = consultMain(archive)

    storeMain(archive, arFinal, errorPerArchive, archivesNames)



Main()