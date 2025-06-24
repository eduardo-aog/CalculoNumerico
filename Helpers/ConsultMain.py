from Helpers.ConsultData import readNumbersData, createDataMatrixFromBins, processSpecialBinFiles
from Repositories.Logger import Logger

def consultMain(archive):
    if archive is None:
        Logger.storeArchiveLog("No se puede leer un archivo vacio")
        exit()

    #Guarda el contenido y al final el nombre de donde estaba
    binArchives, binFilesNames = createDataMatrixFromBins(archive) 
    ecuationMatrix = processSpecialBinFiles(archive)
    arFinal, errorPerArchive = readNumbersData(binArchives)
    return arFinal, errorPerArchive, binFilesNames, ecuationMatrix