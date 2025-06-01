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

def regLin(archive):
    array = numpy.array([0, 0])

    if archive == None:
        print("Object-File: Archivo vacío")
        return array

    lines = numpy.array([])
    n = 0
    aux = 0

    for i in archive:
        n += 1
        lines = numpy.array(i.decode('utf-8').split("#"))
        if(lines.size > aux):
            aux = lines.size

    array[0] = n #filas
    array[1] = aux #columnas
    return array

#Funcion para leer el archivo y guardar los datos en un arreglo
#archive = archive.getArchive()
def readContent(archive, ar):
    i = 0
    for lin in archive:
        reg = numpy.array(lin.decode('utf-8').split("#"))
        for j in range(len(reg)):
            ar[i][j] = reg[j]
        i += 1

'''''''''
Para crear el arreglo donde se guardan los datos
array = numpy.array([2, 3])
ar = numpy.empty(array, dtype=object)
'''''''''