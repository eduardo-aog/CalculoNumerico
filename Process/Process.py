from Repositories.BasesConversion import BasesConversion
from Repositories.NumBases import NumBases
from Repositories.ElementalOperations import ElementalOperations
from Repositories.SignificantDigits import SignificantDigits
from Repositories.CheckEcuationResolvable import CheckEcuationResolvable
from Repositories.MatrixOperations import MatrixOperations
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

def __checkLettersInOperator(self, separateEcuation, isAnyLetter):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(separateEcuation)-1):
            lastBeforeOperator = separateEcuation[i][len(separateEcuation[i])-1]
            firstAfterOperator = separateEcuation[i+1][i]
            isBeforeOperatorLetter = lastBeforeOperator in matrixes
            isAfterOperatorLetter = firstAfterOperator in matrixes
            if not isAnyLetter:
                if (isBeforeOperatorLetter and not isAfterOperatorLetter) or (not isBeforeOperatorLetter and isAfterOperatorLetter): 
                    return False
            else:
                if firstAfterOperator != "0":
                    if isBeforeOperatorLetter or isAfterOperatorLetter:
                        return False
                else:
                    return False
        return True

def convertToDecimal(arFinal):
    for i in range(len(arFinal)):
        for j in range(len(arFinal[i])):
            try:
                if str(arFinal[i][j]) != "nan":
                    if "Binario" not in arFinal[i][j] and "Decimal" not in arFinal[i][j]:
                        separateNumAttributes = arFinal[i][j].split("#")
                        conversion = BasesConversion(separateNumAttributes[0], separateNumAttributes[1])

                        #arFinal[i][j] = strHashNumberFormat(conversion.getNumPossiblyHex())
                        arFinal[i][j] = float(conversion.getNumPossiblyHex())
                    else:
                        arFinal[i][j] = float(arFinal[i][j].split("#")[0])
                else:
                    arFinal[i][j] = 0
            except ValueError as e:
                storeArchiveLog(f"{e.__class__.__name__}/{arFinal[i][j]}/{e}")
            except Exception as e:
                storeArchiveLog(f"{e.__class__.__name__}/{arFinal[i][j]}/{e}")   

def checkEcuations(arFinal, arEcuation):
    convertToDecimal(arFinal)
    for ecuation in arEcuation:
        try:
            currentEcuation = CheckEcuationResolvable(ecuation, len(arFinal))
            if currentEcuation.getResolvable():
                #result = __solveEcuationProccess(ecuation, arFinal)
                pass
            else:
                storeArchiveLog(f"{currentEcuation.getCientificNotation()}/{ecuation}")
        except ValueError as e:
            storeArchiveLog(f"{e.__class__.__name__}/{ecuation}/{e}")
'''''''''''
def __solveBrackets(insideBrackets, arFinal):
    pass

def __solveEcuationProccess(ecuation, arFinal):
    if "(" in ecuation:
        countEcuationBrackets = 0
        for bracket in ecuation:
            if bracket == "(":
                countEcuationBrackets += 1
        for i in range(countEcuationBrackets):
            openBracket = ecuation.split("(")
            openBracket = openBracket[i+1]
            outsideBracket = openBracket[i]
            closedBracket = openBracket.split(")")
            insideBrackets = closedBracket[i]
            outsideBracket = outsideBracket+"RES"+i+closedBracket[i+1]

            bracketsResult = __solveBrackets(insideBrackets, arFinal)
'''''''''''