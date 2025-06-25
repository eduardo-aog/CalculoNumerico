from Repositories.BasesConversion import BasesConversion
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
from Repositories.SignificantDigits import SignificantDigits
from Repositories.CheckEcuationResolvable import CheckEcuationResolvable
from Repositories.SolveEcuation import SolveEcuation
from Repositories.GaussJordan import GaussJordan
from Repositories.GaussSeidel import GaussSeidel
from Repositories.Logger import Logger
import numpy

def replaceString(oldChar, newChar, strToReplace):
    newStr = ""
    if oldChar in strToReplace:
        separateStr = strToReplace.split(oldChar)
        for i in range(len(separateStr)):
            if i < len(separateStr)-1:
                newStr = newStr+separateStr[i]+newChar
            else:
                newStr = newStr+separateStr[i]
        return newStr
    else:
        return strToReplace

def strHashNumberFormat(num):
    bases = NumBases(num)
    operations = ElementalOperations(num)
    digits = SignificantDigits(num)
    return bases.getNum()+"#"+bases.getBase()+"#"+operations.getOperation()+"#"+digits.getNumSignificant()

def emptyVector(space, fill=0):
    emptyV = numpy.empty(space, dtype=object)
    emptyV.fill(fill)
    return emptyV

def emptyMatrix(space1, space2, fill=0):
    emptyM = numpy.empty((space1, space2), dtype=object)
    emptyM.fill(fill)
    return emptyM

def convertToDecimal(arFinal):
    for i in range(len(arFinal)):
        for j in range(len(arFinal[i])):
            try:
                if str(arFinal[i][j]) != "nan":
                    if "Binario" not in arFinal[i][j] and "Decimal" not in arFinal[i][j]:
                        separateNumAttributes = arFinal[i][j].split("#")
                        conversion = BasesConversion(separateNumAttributes[0], separateNumAttributes[1])

                        arFinal[i][j] = float(conversion.getNumPossiblyHex())
                    else:
                        arFinal[i][j] = float(arFinal[i][j].split("#")[0])
                else:
                    arFinal[i][j] = 0
            except ValueError as e:
                Logger.storeArchiveLog(f"{e.__class__.__name__}/{arFinal[i][j]}/{e}", f"{e.__class__.__name__}/{arFinal[i][j]}/{e}")
            except Exception as e:
                Logger.storeArchiveLog(f"{e.__class__.__name__}/{arFinal[i][j]}/{e}", f"{e.__class__.__name__}/{arFinal[i][j]}/{e}")   

def checkEcuations(arFinal:numpy.array, arEcuation:numpy.array):
    i = 0
    convertToDecimal(arFinal)
    results = numpy.empty((len(arEcuation[0]), 1), dtype=object)
    for ecuation in arEcuation:
        try:
            currentEcuation = CheckEcuationResolvable(ecuation)
            if currentEcuation.getResolvable():
                solved = SolveEcuation(ecuation, arFinal)
                results[i] = solved.getResult()
            else:
                Logger.storeArchiveLog(f"{currentEcuation.getCientificNotation()}/{ecuation}",f"{currentEcuation.getCientificNotation()}/{ecuation}")
            i += 1
        except ValueError as e:
            Logger.storeArchiveLog(f"{e.__class__.__name__}/{ecuation}/{e}",f"{e.__class__.__name__}/{ecuation}/{e}")
    results = __gaussJordanSeidel(results)
    return results

def getInputJordanSeidel(text):
    while True:
        try:
            written = int(input(text))
            if written!=0 and written!=1:
                print("Entrada no valida ingresa 0 o 1")
            else:
                return written
        except ValueError:
            print("Entrada no valida ingresa un número entero")

def __gaussJordanSeidel(results:numpy.array):
    optionJordan = getInputJordanSeidel("Realizar operación con Gauss Jordan(0) o Seidel(1): ")
    for i in range(len(results)):
        continue
        matrixB = emptyVector(len(results[i]), 1)
        try:
            if optionJordan==0:
                amplifiedMatrix = GaussJordan.pivoteafila(results[i], matrixB)
                amplifiedMatrix = GaussJordan.gauss_eliminaAdelante(amplifiedMatrix)
                results[i] = GaussJordan.gauss_eliminaAtras(amplifiedMatrix)
            else:
                amplifiedMatrix = GaussSeidel.pivoteaFila(results[i], matrixB)
                results[i] = GaussSeidel.gaussSeidel(results[i], matrixB, amplifiedMatrix)
        except ValueError as e:
            Logger.storeArchiveLog(f"{e.__class__.__name__}/{results[i]}/{e}",f"{e.__class__.__name__}/{results[i]}/{e}")
    return results