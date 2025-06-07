import numpy
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
from Repositories.CifrasSig import CifrasSig

def findBinArchive(archive):
    items = archive.getDirectoriesList()
    for i in items:
        nameArchive = numpy.array(i.split("_"))
        lastItem = len(nameArchive)-1
        if "." in nameArchive[lastItem]:
            if numpy.array(nameArchive[lastItem].split("."))[1]=="bin":
                return nameArchive[lastItem].split(".")[0]

def linesInArchive(archive):
    array = numpy.array([0, 0])

    if archive == None:
        print("Object-File: Archivo vacío")
        return array

    lines = numpy.array([])
    n = 0
    aux = 0

    for i in archive:
        n += 1
        lines = numpy.array(i.split("#"))
        if lines.size > aux:
            aux = lines.size

    array[0] = n #filas
    array[1] = aux #columnas
    return array

def readContent(archive, arraySize):
    i = 0
    if archive == None or arraySize.any == None:
        print("Object-Error: Un objeto es nulo")
        return None
    
    textData = numpy.empty(arraySize, dtype=object)
    for lin in archive:
        reg = numpy.array(lin.split("#"))
        for j in range(len(reg)):
            if "\n" in reg[j]:
                reg[j] = reg[j].split("\n")[0]
                textData[i][j] = reg[j]
            else:
                textData[i][j] = reg[j]
        i += 1
    return textData

def readNumbersData(textData):
    arFinal = numpy.empty(textData.size, dtype=object)
    
    k = 0
    for i in range(len(textData)):
        for j in range(len(textData[i])):
            try:
                if textData[i][j]!="":
                    num = textData[i][j]
                    bases = NumBases(num)
                    operations = ElementalOperations(num)
                    #cifras = CifrasSig(num)
                    arFinal[k] = num+"#"+bases.getBase()+"#"+operations.getOperation()+"#"
                    k += 1
            except (AttributeError, ValueError) as e:
                print(e)
    return arFinal