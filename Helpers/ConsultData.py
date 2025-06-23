import numpy
from Repositories.Logger import storeArchiveLog
from Process.Process import strHashNumberFormat
import os

#funcion luis contar archivos .bin  1)
def countBinFiles(storage_path: str, recursive: bool = True) -> int:
    if not os.path.exists(storage_path):
        raise ValueError(f"Directorio no encontrado: {storage_path}")
    
    count = 0
    if recursive:
        for root, _, files in os.walk(storage_path):
            for file in files:
                if file.endswith('.bin'):
                    count += 1
    else:
        count = len([f for f in os.listdir(storage_path) 
                   if f.endswith('.bin') and os.path.isfile(os.path.join(storage_path, f))])
    
    return count

#funicion que cuenta el valor maximo de registros dentro de todos los archivos . bin 2)
def findMaxRecords(archiveUtil):
    if archiveUtil is None:
        storeArchiveLog("ArchiveUtil no puede ser None")
        exit()
    items = archiveUtil.getDirectoriesList()
    if not items:
        storeArchiveLog("No se encontraron archivos")
        exit()
    
    recordCounts = {}
    maxRecords = -1
    maxFile = ""
    
    for binFile in items:
        if not binFile.endswith('.bin'):
            continue
            
        try:
            content = archiveUtil.getArchive(binFile)
            if content is None:
                continue
                
            # Convertir contenido a texto si es necesario
            if not isinstance(content, str):
                content = '\n'.join(content)
                
            records = content.split('#')
            recordCount = len(records)
            recordCounts[binFile] = recordCount
            
            if recordCount > maxRecords:
                maxRecords = recordCount
                maxFile = binFile
                
        except Exception as e:
            storeArchiveLog(f"Error al procesar {binFile}: {str(e)}")
            recordCounts[binFile] = 0
    
    if maxRecords == -1:
        raise ValueError("No se encontraron archivos .bin válidos")
    
    return maxFile, maxRecords, recordCounts

#Funcion para crear la matrix con los datos de los archivos .bin
def createDataMatrixFromBins(archiveUtil):
    try:
        allBinFiles = archiveUtil.getDirectoriesList()
    except Exception as e:
        print(f"Error al obtener archivos: {e}")
        return None

    # Filtrar archivos .bin sin usar listas
    binFiles = numpy.array([], dtype=object)
    for file in allBinFiles:
        if file.endswith(".bin"):
            binFiles = numpy.append(binFiles, file)

    if binFiles.size == 0:
        storeArchiveLog("No se encontraron archivos .bin")
        return None

    # Obtener máximo número de registros y recuento por archivo
    try:
        _, maxRegistros, _ = findMaxRecords(archiveUtil)
    except Exception as e:
        storeArchiveLog(f"No se pudo determinar el archivo con más registros: {e}")
        return None

    filas = binFiles.size
    columnas = maxRegistros
    matriz = numpy.empty((filas, columnas), dtype=object)
    matriz.fill(numpy.nan)

    for i in range(filas):
        try:
            contenido = archiveUtil.getArchive(binFiles[i])
            if contenido is None:
                continue


            text = '\n'.join(contenido) if not isinstance(contenido, str) else contenido
            
            registers = numpy.array(text.split('#'), dtype=object)

            for j in range(min(registers.size, columnas)):
                matriz[i][j] = registers[j].strip()

        except Exception as e:
            storeArchiveLog(f"Error procesando archivo {binFiles[i]}: {e}")

    return matriz, binFiles

def findBinArchive(archive):
    if archive is None:
        storeArchiveLog("No se puede encontrar un archivo vacio")
        exit()
    
    items = archive.getDirectoriesList()
    if not items:
        storeArchiveLog("No se encontraron directorios")
        exit()
    
    for i in items:
        nameArchive = numpy.array(i.split("_"))
        lastItem = len(nameArchive)-1
        if "." in nameArchive[lastItem]:
            if numpy.array(nameArchive[lastItem].split("."))[1]=="bin":
                return i

def linesInArchive(archive):
    if archive is None:
        storeArchiveLog("No se puede leer un archivo vacio")
        exit()
    
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

def readContent(arrayContent):
    if arrayContent.any == None:
        storeArchiveLog("Object-Error: Un objeto es nulo")
        exit()
    
    for i in arrayContent:
        for j in range(len(arrayContent[i])):
            if "\n" in arrayContent[i]:
                arrayContent[i] = arrayContent[i].split("\n")[0]
        
    return arrayContent

def readNumbersData(binArchives):
    if binArchives.any == None:
        storeArchiveLog("Object-Error: Arreglo es nulo")
        exit()
    errorPerArchive = numpy.empty(len(binArchives),dtype=object)
    errorPerArchive.fill(0)                
    arFinal = numpy.empty((len(binArchives), (len(binArchives[0]))), dtype=object)
    arFinal.fill(numpy.nan)
    
    for i in range(len(binArchives)):
        for j in range(len(binArchives[i])):
            try:
                if str(binArchives[i][j]) != "nan":
                    arFinal[i][j] = strHashNumberFormat(binArchives[i][j])
                else:
                    errorPerArchive[i] += 1
            except ValueError as e:
                storeArchiveLog(f"{e}/{binArchives[i][j]}")
                errorPerArchive[i] += 1
            except Exception as e:
                storeArchiveLog(f"{e}/{binArchives[i][j]}")
                errorPerArchive[i] += 1

    return arFinal, errorPerArchive