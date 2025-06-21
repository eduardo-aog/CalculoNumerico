from Helpers.ConsultData import linesInArchive, readContent, readNumbersData, findBinArchive

def consultMain(archive):
    if archive is None:
        raise ValueError("No se puede leer el archivo vacio")

    nameArchive = findBinArchive(archive)
    lines = linesInArchive(archive.getArchive(nameArchive))
    textData = readContent(archive.getArchive(nameArchive), lines)
    arFinal = readNumbersData(textData)
    return arFinal, nameArchive