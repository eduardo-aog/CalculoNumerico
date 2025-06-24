import numpy
from Repositories.Logger import Logger
from Process.Process import strHashNumberFormat, replaceString, emptyVector, emptyMatrix

#funicion que cuenta el valor maximo de registros dentro de todos los archivos . bin 2)
def __findMaxRecords(archiveUtil):
    if archiveUtil is None:
        Logger.storeArchiveLog("ArchiveUtil no puede ser None")
        exit()
    items = archiveUtil.getDirectoriesList()
    if not items:
        Logger.storeArchiveLog("No se encontraron archivos")
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
            Logger.storeArchiveLog(f"Error al procesar {binFile}: {str(e)}")
            recordCounts[binFile] = 0
    
    if maxRecords == -1:
        raise ValueError("No se encontraron archivos .bin válidos")
    
    return maxFile, maxRecords, recordCounts

#Funcion para crear la matrix con los datos de los archivos .bin
def createDataMatrixFromBins(archiveUtil):
    try:
        allBinFiles = archiveUtil.getDirectoriesList()
    except Exception as e:
        print(f"{e.__class__.__name__}/{e}")
        return None

    # Filtrar archivos .bin sin usar listas
    binFiles = numpy.array([], dtype=object)
    for file in allBinFiles:
        if file.endswith(".bin"):
            binFiles = numpy.append(binFiles, file)

    if binFiles.size == 0:
        Logger.storeArchiveLog("No se encontraron archivos .bin")
        return None

    # Obtener máximo número de registros y recuento por archivo
    try:
        _, maxRegistros, _ = __findMaxRecords(archiveUtil)
    except Exception as e:
        Logger.storeArchiveLog(f"No se pudo determinar el archivo con más registros: {e}")
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
            if "#" in text:
                registers = numpy.array(text.split('#'), dtype=object)

                for j in range(min(registers.size, columnas)):
                    registers[j] = replaceString("\n\n","",registers[j])
                    matriz[i][j] = replaceString(" ","",registers[j])
        except Exception as e:
            Logger.storeArchiveLog(f"{e.__class__.__name__}/{binFiles[i]}/{e}")

    return matriz, binFiles

def processSpecialBinFiles(archiveUtil):
    try:
        allBinFiles = archiveUtil.getDirectoriesList()
    except Exception as e:
        Logger.storeArchiveLog(f"{e.__class__.__name__}/{e}")
        return None

    # Filtrar archivos .bin sin '#'
    specialFiles = {}
    for file in allBinFiles:
        if not file.endswith(".bin"):
            continue
            
        try:
            content = archiveUtil.getArchive(file)
            if content is None:
                continue
                
            # Unificar contenido a string
            textContent = '\n'.join(content) if not isinstance(content, str) else content      
            
            if '#' not in textContent:
                textContent = replaceString(" ","",textContent)
                specialFiles[file] = replaceString("\n\n",",",textContent).split(",")
                
        except Exception as e:
            Logger.storeArchiveLog(f"{e.__class__.__name__}/{file}/{e}")
    
    # Crear matriz si hay archivos especiales
    if not specialFiles:
        return None
    
    # Matriz: filas = archivos, 1 columna con contenido completo
    matriz = numpy.empty(len(specialFiles), dtype=object)
    for i, (file, content) in enumerate(specialFiles.items()):
        matriz[i] = content
    
    return numpy.array(matriz, specialFiles.keys())


def readNumbersData(binArchives):
    if binArchives.any == None:
        Logger.storeArchiveLog("Object-Error: Arreglo es nulo")
        exit()
    errorPerArchive = emptyVector((len(binArchives), 0))     
    arFinal = emptyMatrix(len(binArchives), len(binArchives[0], numpy.nan))               
    
    for i in range(len(binArchives)):
        for j in range(len(binArchives[i])):
            try:
                if str(binArchives[i][j]) != "nan":
                    arFinal[i][j] = strHashNumberFormat(binArchives[i][j])
                else:
                    errorPerArchive[i] += 1
            except ValueError as e:
                Logger.storeArchiveLog(f"{e.__class__.__name__}/{binArchives[i][j]}/{e}")
                errorPerArchive[i] += 1
            except Exception as e:
                Logger.storeArchiveLog(f"{e.__class__.__name__}/{binArchives[i][j]}/{e}")
                errorPerArchive[i] += 1

    return arFinal, errorPerArchive