from Helpers.ConsultData import linesInArchive, readContent, readNumbersData, findBinArchive

def consultMain(archive, binArchive):
    serialRead = findBinArchive(archive)
    lines = linesInArchive(archive.getArchive(binArchive))
    textData = readContent(archive.getArchive(binArchive), lines)
    arFinal = readNumbersData(textData)
    return arFinal, serialRead