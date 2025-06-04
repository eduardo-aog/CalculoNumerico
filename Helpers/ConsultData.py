import numpy
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
from Repositories.CifrasSig import CifrasSig

def findBinArchive(archive):
    if archive is None:
        raise ValueError("No se puede encontrar un archivo vacio")
    
    items = archive.getDirectoriesList()
    if not items:
        raise ValueError("No se encontraron directorios")
    
    for i in items:
        if not isinstance(i, str):
            continue
        parts = i.split("_")
        if "." in parts:
            file_parts = i.split(".")
            if len(file_parts) == 2 and file_parts[1] == "bin":
                return file_parts[0]
    
    raise FileNotFoundError("No se encontró ningún archivo .bin en el directorio")

def linesInArchive(archive):
    if archive is None:
        raise ValueError("No se puede leer un archivo vacio")
    
    array = numpy.array([0, 0])
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
    if archive is None or arraySize is None:
        raise ValueError("No se puede leer un archivo vacio")
    
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
    if textData is None:
        raise ValueError("No se pudo leer el número")
    
    arFinal = numpy.array(textData.size, dtype=object)
    k = 0
    for i in range(len(textData)):
        for j in range(len(textData[i])):
            try:
                if textData[i][j] != "":
                    num = textData[i][j]
                    bases = NumBases.NumBases(num)
                    operations = ElementalOperations.ElementalOperations(num)
                    cifras = CifrasSig.CifrasSig(num)
                    arFinal[k] = num+"#"+bases.getBase()+"#"+operations.getOperation()+"#"+cifras.getCifras()
                    k += 1
            except (AttributeError, ValueError) as e:
                print(f"No es un número válido: {textData[i][j]} - Error: {e}")
            except Exception as e:
                print(f"Error inesperado al procesar {textData[i][j]}: {e}")
    return arFinal