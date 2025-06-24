from Helpers.ConsultMain import consultMain
from Repositories.ArchiveUtil import ArchiveUtil
from Composables.storeMain import storeMain
from Process.ProcessMain import processMain
from Repositories.Logger import Logger
import os

def Main():
    try:
        storageRoute = os.path.dirname(os.path.abspath(__file__))+os.path.sep+"Storage"
        archive = ArchiveUtil(storageRoute)
    except(NotADirectoryError, FileNotFoundError) as e:
        Logger.storeArchiveLog(e+"")
        exit()

    arFinal, errorPerArchive, archivesNames, ecuationMatrix = consultMain(archive)

    storeMain(archive, arFinal, errorPerArchive, archivesNames)

    processMain(archive, ecuationMatrix, arFinal)

Main()