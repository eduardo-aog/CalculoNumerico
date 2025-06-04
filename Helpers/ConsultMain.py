from Helpers.ConsultData import linesInArchive, readContent, readNumbersData, findBinArchive

def consultMain(archive, binArchive):
    if archive is None:
        raise ValueError("No se puede leer un archivo vacio")
        
    if binArchive is None:
        raise ValueError("No se puede leer un archivo binario vacio")

    serialRead = findBinArchive(archive)
    lines = linesInArchive(archive.getArchive(binArchive))
    textData = readContent(archive.getArchive(binArchive), lines)
    arFinal = readNumbersData(textData)
    return arFinal, serialRead