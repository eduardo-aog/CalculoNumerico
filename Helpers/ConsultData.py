import numpy
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
import os
import glob
from typing import Dict, Tuple #agregado por luisimport numpy as np
from typing import Optional
import numpy as np
#from Repositories.CifrasSig import CifrasSig

#funcion luis contar archivos .bin  1)
def count_bin_files(storage_path: str, recursive: bool = True) -> int:
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

def find_max_records(archive_util) -> Tuple[str, int, Dict[str, int]]:

    if archive_util is None:
        raise ValueError("ArchiveUtil no puede ser None")
    
    items = archive_util.getDirectoriesList()
    if not items:
        raise ValueError("No se encontraron archivos")
    
    record_counts = {}
    max_records = -1
    max_file = ""
    
    for bin_file in items:
        if not bin_file.endswith('.bin'):
            continue
            
        try:
            content = archive_util.getArchive(bin_file)
            if content is None:
                continue
                
            # Convertir contenido a texto si es necesario
            if not isinstance(content, str):
                content = '\n'.join(content)
                
            records = content.split('#')
            record_count = len(records)
            record_counts[bin_file] = record_count
            
            if record_count > max_records:
                max_records = record_count
                max_file = bin_file
                
        except Exception as e:
            print(f"Error al procesar {bin_file}: {str(e)}")
            record_counts[bin_file] = 0
    
    if max_records == -1:
        raise ValueError("No se encontraron archivos .bin válidos")
    
    return max_file, max_records, record_counts

#Funcion para crear la matrix con los datos de los archivos .bin

def create_data_matrix_from_bins(archive_util) -> Optional[np.ndarray]:
    try:
        all_bin_files = archive_util.getDirectoriesList()
    except Exception as e:
        print(f"Error al obtener archivos: {e}")
        return None

    # Filtrar archivos .bin sin usar listas
    bin_files = np.array([], dtype=object)
    for file in all_bin_files:
        if file.endswith(".bin"):
            bin_files = np.append(bin_files, file)

    if bin_files.size == 0:
        print("No se encontraron archivos .bin")
        return None

    # Obtener máximo número de registros y recuento por archivo
    try:
        _, max_registros, _ = find_max_records(archive_util)
    except Exception as e:
        print(f"No se pudo determinar el archivo con más registros: {e}")
        return None

    filas = bin_files.size
    columnas = max_registros
    matriz = np.empty((filas, columnas), dtype=object)
    matriz.fill(np.nan)

    for i in range(filas):
        try:
            contenido = archive_util.getArchive(bin_files[i])
            if contenido is None:
                continue

            texto = '\n'.join(contenido) if not isinstance(contenido, str) else contenido
            registros = np.array(texto.split('#'), dtype=object)

            for j in range(min(registros.size, columnas)):
                matriz[i, j] = registros[j].strip()

        except Exception as e:
            print(f"Error procesando archivo {bin_files[i]}: {e}")

    return matriz




def findBinArchive(archive):
    if archive is None:
        raise ValueError("No se puede encontrar un archivo vacio")
    
    items = archive.getDirectoriesList()
    if not items:
        raise ValueError("No se encontraron directorios")
    
    for i in items:
        nameArchive = numpy.array(i.split("_"))
        lastItem = len(nameArchive)-1
        if "." in nameArchive[lastItem]:
            if numpy.array(nameArchive[lastItem].split("."))[1]=="bin":
                return nameArchive[lastItem].split(".")[0]

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
    if textData.any == None:
        print("Object-Error: Arreglo es nulo")
        return None
    
    arFinal = numpy.empty(textData.size, dtype=object)
    
    k = 0
    for i in range(len(textData)):
        for j in range(len(textData[i])):
            try:
                if textData[i][j] != "":
                    num = textData[i][j]
                    bases = NumBases(num)
                    operations = ElementalOperations(num)
                    #cifras = CifrasSig(num)
                    arFinal[k] = num+"#"+bases.getBase()+"#"+operations.getOperation()+"#"
                    k += 1
            except (AttributeError, ValueError) as e:
                print(f"No es un número válido: {textData[i][j]} - Error: {e}")
            except Exception as e:
                print(f"Error inesperado al procesar {textData[i][j]}: {e}")
    return arFinal