from Repositories.MatrixOperations import MatrixOperations
import numpy

class SolveEcuation:
    def __init__(self, ecuation, arFinal):
        self.__utilSolve(ecuation, arFinal)

    def __emptyMatrix(self, space1, space2, fill=0):
        emptyM = numpy.empty((space1, space2), dtype=object)
        emptyM.fill(fill)
        return emptyM

    def __countOperator(ecuation, operators):
        count = 0
        for value in ecuation:
            for n in operators:
                if value == n:
                    count += 1
        return count  

    def __separateBracketsProcess(self, ecuation, i):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if self.__countOperator(ecuation, matrixes)>0:
            openBracket = ecuation.split("(")
            openBracket = openBracket[i+1]
            outsideBracket1 = openBracket[i]
            closedBracket = openBracket.split(")")
            insideBrackets = closedBracket[i]
            outsideBracket = outsideBracket1+"#"+i+closedBracket[i+1]
            return insideBrackets, outsideBracket
        else:
            openBracket = ecuation.split("(")
            openBracket = openBracket[i+1]
            outsideBracket1 = openBracket[i]
            closedBracket = openBracket.split(")")
            insideBrackets = closedBracket[i]
            outsideBracket = outsideBracket1+self.__solveBrackets(insideBrackets, allNumber=True)+closedBracket[i+1]
            return "#", outsideBracket
        
    def __whichSideMatrix(self, firstValue, secondValue):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            
        isBeforeOperatorLetter = firstValue in matrixes
        isAfterOperatorLetter = secondValue in matrixes
        if isBeforeOperatorLetter and not isAfterOperatorLetter: 
            return "L"
        elif not isBeforeOperatorLetter and isAfterOperatorLetter:
            return "R"

    def __asignArchToMatrix(self, matrixToOperate):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        i = 0
        for letter in matrixes:
            if letter == matrixToOperate:
                return i
            i += 1
        return None

    def __solveBrackets(self, insideBrackets, arFinal=None, allNumber=False):
        if arFinal==None and allNumber==False:
            raise ValueError("No se pueden aplicar operaciones de matrices sin arreglos")
        
        lastLeft = len(insideBrackets[0])-1
        if "/" in insideBrackets and allNumber:
            insideBrackets = insideBrackets.split("/")
            return insideBrackets[0][lastLeft]/insideBrackets[1][0]
        if "x" in insideBrackets:
            insideBrackets = insideBrackets.split("x")
            matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            return MatrixOperations.matrixMult(arFinal[matrixAPosition], arFinal[matrixBPosition])
        if "*" in insideBrackets:
            insideBrackets = insideBrackets.split("*")
            if allNumber:
                return int(insideBrackets[0][lastLeft]) * int(insideBrackets[1][0])
            side = self.__whichSideMatrix(insideBrackets[0][lastLeft], insideBrackets[1][0])
            if side=="L":
                matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
                return MatrixOperations.matrixScalarMult(arFinal[matrixAPosition], insideBrackets[1][0])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            return MatrixOperations.matrixScalarMult(insideBrackets[0][lastLeft], arFinal[matrixBPosition])
        if "+" in insideBrackets:
            if allNumber:
                return int(insideBrackets[0][lastLeft]) + int(insideBrackets[1][0])
            insideBrackets = insideBrackets.split("+")
            if len(insideBrackets)==2:
                matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
                matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
                return MatrixOperations.matrixSum(arFinal[matrixAPosition], arFinal[matrixBPosition])
            else:
                totalMatrix = self.__emptyMatrix(len(arFinal), len(arFinal[0]), 0)
                for i in range(len(insideBrackets)-1):
                    matrixAPosition = self.__asignArchToMatrix(insideBrackets[i][lastLeft])
                    matrixBPosition = self.__asignArchToMatrix(insideBrackets[i+1][i])
                    totalMatrix = MatrixOperations.matrixSum(MatrixOperations.matrixSum(arFinal[matrixAPosition], arFinal[matrixBPosition]), totalMatrix)
                return totalMatrix
        if "-" in insideBrackets:
            insideBrackets = insideBrackets.split("-")
            if allNumber:
                return int(insideBrackets[0][lastLeft]) - int(insideBrackets[1][0])
            matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            return MatrixOperations.matrixMinus(arFinal[matrixAPosition], arFinal[matrixBPosition])
        return None
    
    def __removeLastOrFisrt(string, last):
        newStr = ""
        if last:
            for i in range(len(string)-1):
                newStr = newStr+string[i]
            return newStr
        else:
            for i in range(len(string)-1):
                newStr = newStr+string[i+1]
        return newStr

    def __joinEcuationLeft(self, ecuationLeftSolving, j, operator):
        ecuationLeftSolving[0] = self.__removeLastOrFisrt(ecuationLeftSolving[0], True)
        ecuationLeftSolving[1] = self.__removeLastOrFisrt(ecuationLeftSolving[1], False)
        if len(ecuationLeftSolving)>2:
            rightSide = ""
            for i in range(len(ecuationLeftSolving)-2):
                rightSide = rightSide+operator+ecuationLeftSolving[i+2]
            return ecuationLeftSolving[0]+"#"+j+ecuationLeftSolving[1]+rightSide
        else:
            return ecuationLeftSolving[0]+"#"+j+ecuationLeftSolving[1]

    def __splitDependingOperator(self, ecuation, j):
        for i in ecuation:
            if "/" == i:
                return self.__joinEcuationLeft(ecuation.split("/"), j, "/")
            if "x" == i:
                return self.__joinEcuationLeft(ecuation.split("x"), j, "x")
            if "*" == i:
                return self.__joinEcuationLeft(ecuation.split("*"), j, "*")
            if "+" == i:
                return self.__joinEcuationLeft(ecuation.split("+"), j, "+")
            if "-" == i:
                return self.__joinEcuationLeft(ecuation.split("-"), j, "-")
    
    def __solveWithHash(self, ecuation, arFinal, arAcumulated):
        lastLeft = len(ecuation[0])-1
        if "/" in ecuation:
            insideBrackets = ecuation.split("/")
            return insideBrackets[0][lastLeft]/insideBrackets[1][0]
        if "x" in ecuation:
            insideBrackets = ecuation.split("x")
            matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            if matrixAPosition==None:
                return MatrixOperations.matrixMult(arAcumulated[int(insideBrackets[0][lastLeft])], arFinal[matrixBPosition])
            return MatrixOperations.matrixMult(arFinal[matrixAPosition], arAcumulated[int(insideBrackets[1][1])])
        if "*" in ecuation:
            insideBrackets = ecuation.split("*")
            side = self.__whichSideMatrix(insideBrackets[0][lastLeft], insideBrackets[1][0])
            if side=="L":
                matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
                if matrixAPosition==None:
                    return MatrixOperations.matrixScalarMult(arAcumulated[int(insideBrackets[0][lastLeft])], insideBrackets[1][0])
                return MatrixOperations.matrixScalarMult(arFinal[matrixAPosition], insideBrackets[1][0])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            if matrixBPosition==None:
                return MatrixOperations.matrixScalarMult(insideBrackets[0][lastLeft], arAcumulated[int(insideBrackets[1][1])])
            return MatrixOperations.matrixScalarMult(insideBrackets[0][lastLeft], arFinal[matrixBPosition])
        if "+" in ecuation:
            insideBrackets = ecuation.split("+")
            matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            if matrixAPosition==None:
                return MatrixOperations.matrixSum(arAcumulated[int(insideBrackets[0][lastLeft])], arFinal[matrixBPosition])
            return MatrixOperations.matrixSum(arFinal[matrixAPosition], arAcumulated[int(insideBrackets[1][1])])
        if "-" in ecuation:
            insideBrackets = ecuation.split("-")
            matrixAPosition = self.__asignArchToMatrix(insideBrackets[0][lastLeft])
            matrixBPosition = self.__asignArchToMatrix(insideBrackets[1][0])
            if matrixAPosition==None:
                return MatrixOperations.matrixMinus(arAcumulated[int(insideBrackets[0][lastLeft])], arFinal[matrixBPosition])
            return MatrixOperations.matrixMinus(arFinal[matrixAPosition], arAcumulated[int(insideBrackets[1][1])])
        return None
    
    def __utilSolve(self, ecuation, arFinal):
        operators = "/*x-+"
        outsideBracket = ""
        totalMatrix = self.__emptyMatrix(len(arFinal[0]), 1, 0)
        if "(" in ecuation:
            numberBrackets = self.__countOperator(ecuation, "(")
            resultsBrackets = self.__emptyMatrix(numberBrackets, 1, 0)
            for i in range(numberBrackets-1):
                if "#" not in outsideBracket:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(ecuation, i)
                    if insideBrackets!="#":             
                        resultsBrackets[i] = self.__solveBrackets(insideBrackets, arFinal)
                else:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(outsideBracket, i)
                    if insideBrackets!="#":                 
                        resultsBrackets[i] = self.__solveBrackets(insideBrackets, arFinal)

            toOperate = self.__countOperator(ecuation, operators)

            totalMatrix = self.__solveBrackets(outsideBracket)            
        else:
            toOperate = self.__countOperator(ecuation, operators)
            for i in range(toOperate):
                if i==0:
                    outsideBracket = self.__splitDependingOperator(ecuation, i)
                    totalMatrix[i] = self.__solveBrackets(ecuation)
                else:
                    totalMatrix[i] = self.__solveWithHash(outsideBracket)
                    outsideBracket = self.__splitDependingOperator(outsideBracket, i)


        return totalMatrix