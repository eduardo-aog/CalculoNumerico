import numpy
from Repositories import ArchiveUtil
from Repositories import NumBases
from Repositories import ElementalOperations


def showCase(measuredValue, realValue, absoluteError, relativeError):
    print("Valor medido: ",measuredValue)
    print("Valor real: ", realValue)
    print("Error absoluto de la medida: ",absoluteError)
    print("Error relativo de la medida: ",relativeError)
    print("Error relativo de la medida en porcentaje: ",relativeError*100,"% ")

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
    if archive == None or arraySize == None:
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