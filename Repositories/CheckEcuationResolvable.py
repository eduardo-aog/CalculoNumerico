class CheckEcuationResolvable:
    def __init__(self, ecuation, numberOfArchives):
        self.__utilValNumber(numberOfArchives)
        self.__utilValEcuationFormat(ecuation)
        self.__utilResolvable()

    def  __utilValNumber(self, numberOfArchives):
        if numberOfArchives == None:
            raise ValueError("No se permite un valor nulo")
        if type(numberOfArchives) != int:
            raise ValueError("No se permite no entero")
        if numberOfArchives < 1:
            raise ValueError("No se permite un valor menor a uno")
        self.__numberOfArchives = numberOfArchives
    
    def __utilValEcuationFormat(self, ecuation):
        if ecuation == None:
            raise ValueError("No se permite un valor nulo")
        if not self.__checkSpecialChars(ecuation):
            raise ValueError("No se permite caracteres no validos")
        if not self.__utilValBracketsFormat(ecuation):
            raise ValueError("No se permite un formato no valido de parentesis")
        self.__ecuation = ecuation

    def __utilResolvable(self):
        self.__resolvable, reason = self.__isEcuationResolvable()
        #Dar la razon de si es o no resolvible (Notación científica)
        self.__cientificNotation = reason
        
    def __utilValBracketsFormat(self, ecuation):
        if ("(" in ecuation and ")" not in ecuation) or (")" in ecuation and "(" not in ecuation):
            return False
        if ("[" in ecuation and "]" not in ecuation) or ("]" in ecuation and "[" not in ecuation):
            return False
        if ("{" in ecuation and "}" not in ecuation) or ("}" in ecuation and "{" not in ecuation):
            return False
        return True

    def __oneInOtherNotIn(self, compare1, compare2, compareInEcuation):
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

    def __checkLettersInOperator(self, separateEcuation, matrixes, isAnyLetter):
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

    def __isEcuationResolvable(self):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        resolvable = True

        #Casos con solo o números o matrices(sin división)
        allNumbers = self.__oneInOtherNotIn(numbers, matrixes, self.__ecuation)
        allMatrixNoDiv = self.__oneInOtherNotIn(matrixes, numbers, self.__ecuation) and "/" not in self.__ecuation
        resolvable = allNumbers or allMatrixNoDiv
        if resolvable:
            return resolvable, "all num/matrix(no div)"
        
        resolvable = True
        #Caso con suma
        if "+" in self.__ecuation:
            separateEcuation = self.__ecuation.split("+")
            resolvable = self.__checkLettersInOperator(separateEcuation, matrixes, False)
        if not resolvable:
            return resolvable, "not possible +"
        #Caso con resta
        if "-" in self.__ecuation:
            separateEcuation = self.__ecuation.split("-")
            resolvable = self.__checkLettersInOperator(separateEcuation, matrixes, False)
        if not resolvable:
            return resolvable, "not possible -"
        #Caso con división
        if "/" in self.__ecuation:
            separateEcuation = self.__ecuation.split("/")
            resolvable = self.__checkLettersInOperator(separateEcuation, matrixes, True)
        if not resolvable:
            return resolvable, "not possible /(Div matrix or Div 0)"
        #Revisar si el número de archivos es menor al de matrices en la ecuación
        countEcuationMatrixes = 0
        for letter in matrixes:
            if letter in self.__ecuation:
                countEcuationMatrixes += 1
        if countEcuationMatrixes < self.__numberOfArchives:
            resolvable = False
            return resolvable, "not enough arch"

        return resolvable, "is possible"
    
    def __checkSpecialChars(self, ecuation):
        specialChars = "|°¬!#$%&?¡'¿´;:_¨* "
        for i in ecuation:
            if i.lower() in specialChars:
                return False
        return True

    def getEcuation(self):
        return self.__ecuation
    
    def getNumberOfArchives(self):
        return self.__numberOfArchives
    
    def getResolvable(self):
        return self.__resolvable
    
    def getCientificNotation(self):
        return self.__cientificNotation