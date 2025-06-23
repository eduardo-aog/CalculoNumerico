from Helpers.ConsultData import linesInArchive, readContent, readNumbersData, findBinArchive, createDataMatrixFromBins
from Repositories.Logger import storeArchiveLog

def consultMain(archive):
    if archive is None:
        storeArchiveLog("No se puede leer un archivo vacio")
        exit()

    #Guarda el contenido y al final el nombre de donde estaba
    binArchives, binFilesNames = createDataMatrixFromBins(archive) 

    #nameArchive = findBinArchive(archive)
    #lines = linesInArchive(archive.getArchive(nameArchive))
    #textData = readContent(archive.getArchive(nameArchive), lines)
    arFinal, errorPerArchive = readNumbersData(binArchives)
    return arFinal, errorPerArchive, binFilesNames