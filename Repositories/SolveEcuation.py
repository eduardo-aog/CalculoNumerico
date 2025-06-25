from Repositories.MatrixOperations import MatrixOperations
import numpy

class SolveEcuation:
    def __init__(self, ecuation, arFinal):
        self.__ecuation = ecuation
        self.__arFinal = arFinal
        self.__result = self.__solveEcuation()
    
    def __createEmptyArray(self, size):
        """Crea un array vacío de tamaño especificado"""
        emptyArray = numpy.empty(size, dtype=object)
        for i in range(size):
            emptyArray[i] = None
        return emptyArray
    
    def __createEmptyMatrix(self, rows, cols):
        """Crea una matriz vacía de tamaño especificado"""
        emptyMatrix = numpy.empty((rows, cols), dtype=object)
        for i in range(rows):
            for j in range(cols):
                emptyMatrix[i][j] = None
        return emptyMatrix
    
    def __isDigit(self, char):
        """Verifica si un carácter es un dígito"""
        digits = "0123456789"
        for digit in digits:
            if char == digit:
                return True
        return False
    
    def __isLetter(self, char):
        """Verifica si un carácter es una letra (matriz)"""
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for letter in letters:
            if char == letter:
                return True
        return False
    
    def __isOperator(self, char):
        """Verifica si un carácter es un operador"""
        operators = "+-*/x"
        for operator in operators:
            if char == operator:
                return True
        return False
    
    def __isBracket(self, char):
        """Verifica si un carácter es un paréntesis o corchete"""
        brackets = "()[]"
        for bracket in brackets:
            if char == bracket:
                return True
        return False
    
    def __extractNumber(self, ecuation, startIndex):
        """Extrae un número completo desde un índice"""
        number = ""
        i = startIndex
        while i < len(ecuation) and (self.__isDigit(ecuation[i]) or ecuation[i] == '.'):
            number = number + ecuation[i]
            i = i + 1
        return number, i - 1
    
    def __extractMatrix(self, ecuation, startIndex):
        """Extrae una matriz (letra) desde un índice"""
        matrix = ""
        i = startIndex
        while i < len(ecuation) and self.__isLetter(ecuation[i]):
            matrix = matrix + ecuation[i]
            i = i + 1
        return matrix, i - 1
    
    def __getMatrixIndex(self, matrixName):
        """Obtiene el índice de una matriz en el arreglo final"""
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(len(letters)):
            if letters[i] == matrixName:
                return i
        return -1
    
    def __getMatrixFromArray(self, matrixName):
        """Obtiene la matriz desde el arreglo final"""
        index = self.__getMatrixIndex(matrixName)
        if index >= 0 and index < len(self.__arFinal):
            return self.__arFinal[index]
        return None
    
    def __convertStringToNumber(self, numberStr):
        """Convierte un string a número"""
        if "." in numberStr:
            parts = numberStr.split(".")
            integerPart = 0
            decimalPart = 0

            for i in range(len(parts[0])):
                digit = int(parts[0][i])
                power = len(parts[0]) - i - 1
                integerPart = integerPart + digit * (10 ** power)

            for i in range(len(parts[1])):
                digit = int(parts[1][i])
                power = -(i + 1)
                decimalPart = decimalPart + digit * (10 ** power)
            
            return integerPart + decimalPart
        else:
            result = 0
            for i in range(len(numberStr)):
                digit = int(numberStr[i])
                power = len(numberStr) - i - 1
                result = result + digit * (10 ** power)
            return result
    
    def __parseEcuation(self, ecuation):
        """Parsea la ecuación en tokens"""
        tokens = self.__createEmptyArray(len(ecuation) * 2)
        tokenCount = 0
        i = 0
        
        while i < len(ecuation):
            char = ecuation[i]
            
            if char == " ":
                i = i + 1
                continue
            
            if self.__isDigit(char):
                number, endIndex = self.__extractNumber(ecuation, i)
                tokens[tokenCount] = {"type": "number", "value": number}
                tokenCount = tokenCount + 1
                i = endIndex + 1
            
            elif self.__isLetter(char):
                matrix, endIndex = self.__extractMatrix(ecuation, i)
                tokens[tokenCount] = {"type": "matrix", "value": matrix}
                tokenCount = tokenCount + 1
                i = endIndex + 1
            
            elif self.__isOperator(char):
                tokens[tokenCount] = {"type": "operator", "value": char}
                tokenCount = tokenCount + 1
                i = i + 1
            
            elif self.__isBracket(char):
                tokens[tokenCount] = {"type": "bracket", "value": char}
                tokenCount = tokenCount + 1
                i = i + 1
            
            else:
                i = i + 1

        finalTokens = self.__createEmptyArray(tokenCount)
        for j in range(tokenCount):
            finalTokens[j] = tokens[j]
        
        return finalTokens
    
    def __findMatchingBracket(self, tokens, startIndex):
        """Encuentra el paréntesis o corchete de cierre correspondiente"""
        openBracket = tokens[startIndex]["value"]
        closeBracket = ")"
        if openBracket == "[":
            closeBracket = "]"
        
        count = 1
        i = startIndex + 1
        
        while i < len(tokens) and count > 0:
            if tokens[i]["type"] == "bracket":
                if tokens[i]["value"] == openBracket:
                    count = count + 1
                elif tokens[i]["value"] == closeBracket:
                    count = count - 1
            i = i + 1
        
        return i - 1
    
    def __evaluateSimpleOperation(self, left, right, operator):
        """Evalúa una operación simple entre dos valores"""
        if isinstance(left, (int, float)) and isinstance(right, (int, float)):
            if operator == "+":
                return left + right
            elif operator == "-":
                return left - right
            elif operator == "*":
                return left * right
            elif operator == "/":
                if right == 0:
                    raise ValueError("División por cero")
                return left / right

        elif left is not None and right is not None and not isinstance(left, (int, float)) and not isinstance(right, (int, float)):
            matrixOps = MatrixOperations()
            if operator == "+":
                return matrixOps.matrixSum(left, right)
            elif operator == "-":
                return matrixOps.matrixMinus(left, right)
            elif operator == "x":
                return matrixOps.matrixMult(left, right)
            elif operator == "/":
                raise ValueError("No se puede dividir matrices")

        elif operator == "*":
            matrixOps = MatrixOperations()
            if isinstance(left, (int, float)) and right is not None and not isinstance(right, (int, float)):
                return matrixOps.matrixScalarMult(right, left)
            elif isinstance(right, (int, float)) and left is not None and not isinstance(left, (int, float)):
                return matrixOps.matrixScalarMult(left, right)
        
        raise ValueError(f"Operación no válida: {operator}")
    
    def __evaluateExpression(self, tokens, startIndex, endIndex):
        """Evalúa una expresión sin paréntesis respetando el orden de operaciones"""
        if startIndex > endIndex:
            return None

        i = startIndex
        while i <= endIndex:
            if tokens[i]["type"] == "operator" and (tokens[i]["value"] == "*" or tokens[i]["value"] == "/" or tokens[i]["value"] == "x"):
                leftToken = tokens[i - 1]
                rightToken = tokens[i + 1]
                
                left = None
                right = None
                
                if leftToken["type"] == "number":
                    left = self.__convertStringToNumber(leftToken["value"])
                elif leftToken["type"] == "matrix":
                    left = self.__getMatrixFromArray(leftToken["value"])
                
                if rightToken["type"] == "number":
                    right = self.__convertStringToNumber(rightToken["value"])
                elif rightToken["type"] == "matrix":
                    right = self.__getMatrixFromArray(rightToken["value"])
                
                result = self.__evaluateSimpleOperation(left, right, tokens[i]["value"])
                
                tokens[i - 1] = {"type": "number", "value": str(result)}
                tokens[i] = {"type": "operator", "value": "+"}
                tokens[i + 1] = {"type": "number", "value": "0"}

                endIndex = endIndex - 2
                i = i - 1
            
            i = i + 1

        i = startIndex
        while i <= endIndex:
            if tokens[i]["type"] == "operator" and (tokens[i]["value"] == "+" or tokens[i]["value"] == "-"):
                leftToken = tokens[i - 1]
                rightToken = tokens[i + 1]
                
                left = None
                right = None
                
                if leftToken["type"] == "number":
                    left = self.__convertStringToNumber(leftToken["value"])
                elif leftToken["type"] == "matrix":
                    left = self.__getMatrixFromArray(leftToken["value"])
                
                if rightToken["type"] == "number":
                    right = self.__convertStringToNumber(rightToken["value"])
                elif rightToken["type"] == "matrix":
                    right = self.__getMatrixFromArray(rightToken["value"])
                
                result = self.__evaluateSimpleOperation(left, right, tokens[i]["value"])
                
                tokens[i - 1] = {"type": "number", "value": str(result)}
                tokens[i] = {"type": "operator", "value": "+"}
                tokens[i + 1] = {"type": "number", "value": "0"}
                
                endIndex = endIndex - 2
                i = i - 1
            
            i = i + 1

        if startIndex <= endIndex:
            finalToken = tokens[startIndex]
            if finalToken["type"] == "number":
                return self.__convertStringToNumber(finalToken["value"])
            elif finalToken["type"] == "matrix":
                return self.__getMatrixFromArray(finalToken["value"])
        
        return None
    
    def __evaluateBrackets(self, tokens, startIndex, endIndex):
        """Evalúa una expresión con paréntesis"""
        if startIndex > endIndex:
            return None

        i = startIndex
        while i <= endIndex:
            if tokens[i]["type"] == "bracket" and (tokens[i]["value"] == "(" or tokens[i]["value"] == "["):

                closeIndex = self.__findMatchingBracket(tokens, i)

                innerResult = self.__evaluateBrackets(tokens, i + 1, closeIndex - 1)

                tokens[i] = {"type": "number", "value": str(innerResult)}

                for j in range(i + 1, closeIndex + 1):
                    tokens[j] = {"type": "operator", "value": "+"}

                endIndex = endIndex - (closeIndex - i)

                continue
            
            i = i + 1

        return self.__evaluateExpression(tokens, startIndex, endIndex)
    
    def __solveEcuation(self):
        """Resuelve la ecuación completa"""
        try:
            tokens = self.__parseEcuation(self.__ecuation)

            result = self.__evaluateBrackets(tokens, 0, len(tokens) - 1)
            
            return result
            
        except Exception as e:
            print(f"Error al resolver la ecuación: {e}")
            return None
    
    def getResult(self):
        """Retorna el resultado de la ecuación"""
        return self.__result