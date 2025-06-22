from Repositories.BasesConversion import BasesConversion
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
from Repositories.SignificantDigits import SignificantDigits
from Repositories.Logger import storeArchiveLog

def aproxValue(values):
    if values != None:
        sum = 0
        for i in values:
            for k in i:
                sum += k
        average = sum / 12
        return average
    else:
        print("Datos nulos. Fin del programa")

def exactValue(values):
    if values != None:
        sum = 0
        ki = 0
        for i in values:
            for k in i:
                ki = k+0.01
                sum += ki
        average = sum / 12
        return average
    else:
        print("Datos nulos. Fin del programa")

def strHashNumberFormat(num):
    bases = NumBases(num)
    operations = ElementalOperations(num)
    digits = SignificantDigits(num)
    return num+"#"+bases.getBase()+"#"+operations.getOperation()+"#"+digits.getNumSignificant()

def convertToDecimal(arFinal):
    for i in range(len(arFinal)):
        for j in range(len(arFinal[i])):
            try:
                if arFinal[i][j] != "nan":
                    if "Binario" not in arFinal[i][j] and "Decimal" not in arFinal[i][j]:
                        separateNumAttributes = arFinal[i][j].split("#")
                        conversion = BasesConversion(separateNumAttributes[0], separateNumAttributes[1])

                        arFinal[i][j] = strHashNumberFormat(conversion.getNumPossiblyHex())
            except ValueError as e:
                storeArchiveLog(f"No es un numero valido: {arFinal[i][j]} - Error: {e}")
            except Exception as e:
                storeArchiveLog(f"Error inesperado al procesar {arFinal[i][j]}: {e}")

def __oneInOtherOneNotIn(compare1, compare2, compareInEcuation):
    for n1 in compare1:
        for n2 in compare2:
            if n1 in compareInEcuation and n2 not in compareInEcuation:
                possible = True
            else:
                possible = False
                break
        if not possible:
            break
    return possible

def __checkLettersInOperator(separateEcuation, matrixes, isAnyLetter):
    for i in range(len(separateEcuation)-1):
        lastBeforeOperator = separateEcuation[i][len(separateEcuation[i])-1]
        firstAfterOperator = separateEcuation[i+1][i]
        isBeforeOperatorLetter = lastBeforeOperator in matrixes
        isAfterOperatorLetter = firstAfterOperator in matrixes

        if not isAnyLetter:
            if (isBeforeOperatorLetter and not isAfterOperatorLetter) or (not isBeforeOperatorLetter and isAfterOperatorLetter): 
                return False
        else:
            if isBeforeOperatorLetter or isAfterOperatorLetter:
                return False
    return True

def __checkSpecialChars(ecuation):
    specialChars = "|°¬!#$%&?¡'¿´;:_¨* "
    for i in ecuation:
        if i.lower() in specialChars:
            return False
    return True
    

def checkIsEcuationResolvable(ecuation, numberOfArchives):
    matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    resolvable = True

    if not __checkSpecialChars(ecuation):
        return False
    if "(" in ecuation and ")" not in ecuation or ")" in ecuation and "(" not in ecuation:
        return False
    else:
        #Casos con solo o números o matrices(sin división)
        allNumbers = __oneInOtherOneNotIn(numbers, matrixes, ecuation)
        allMatrixNoDiv = __oneInOtherOneNotIn(matrixes, numbers, ecuation) and "/" not in ecuation
        resolvable = allNumbers or allMatrixNoDiv
        if resolvable:
            return resolvable
        
        resolvable = True
        #Caso con suma
        if "+" in ecuation:
            separateEcuation = ecuation.split("+")
            resolvable = __checkLettersInOperator(separateEcuation, matrixes, False)
        if not resolvable:
            return resolvable
        #Caso con resta
        if "-" in ecuation:
            separateEcuation = ecuation.split("-")
            resolvable = __checkLettersInOperator(separateEcuation, matrixes, False)
        if not resolvable:
            return resolvable
        #Caso con división
        if "/" in ecuation:
            separateEcuation = ecuation.split("/")
            resolvable = __checkLettersInOperator(separateEcuation, matrixes, True)
        if not resolvable:
            return resolvable
        #Revisar si el número de archivos es menor al de matrices en la ecuación
        countEcuationMatrixes = 0
        for letter in matrixes:
            if letter in ecuation:
                countEcuationMatrixes += 1
        if countEcuationMatrixes < numberOfArchives:
            resolvable = False

        return resolvable        

def solveEcuations(arFinal, arEcuation):
    convertToDecimal(arFinal)
    for ecuation in arEcuation:
        if checkIsEcuationResolvable(ecuation, len(arFinal)):
            #Proceso de resolución
            pass 
        else:
            storeArchiveLog(f"No es una ecuación valida: {ecuation}")

