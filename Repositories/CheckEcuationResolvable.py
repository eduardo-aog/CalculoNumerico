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
        self.__resolvable, reason = self.__isItResolvable()
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
            outsideBracket = outsideBracket1+"A"+closedBracket[i+1]
            return insideBrackets, outsideBracket
        else:
            openBracket = ecuation.split("(")
            openBracket = openBracket[i+1]
            outsideBracket1 = openBracket[i]
            closedBracket = openBracket.split(")")
            insideBrackets = closedBracket[i]
            outsideBracket = outsideBracket1+"1"+closedBracket[i+1]
            return insideBrackets, outsideBracket
    
    def __isItResolvable(self):
        if "(" in self.__ecuation:
            numberBrackets = self.__countOperator(self.__ecuation, "(")
            for i in range(numberBrackets):
                if i==0:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(self.__ecuation, i)                
                    resolvable, reason = self.__isEcuationResolvableProcess(insideBrackets)
                    if not resolvable:
                        return resolvable, reason
                else:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(outsideBracket, i)                
                    resolvable, reason = self.__isEcuationResolvableProcess(insideBrackets)
                    if not resolvable:
                        return resolvable, reason
            resolvable, reason = self.__isEcuationResolvableProcess(outsideBracket)            
        else:
            resolvable, reason = self.__isEcuationResolvableProcess(self.__ecuation)

        return resolvable, reason

    def __isEcuationResolvableProcess(self, ecuation):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        resolvable = True

        #Casos con solo o números o matrices(sin división y mult escalar)
        allNumbers = self.__oneInOtherNotIn(numbers, matrixes, ecuation)
        allMatrixNoDiv = self.__oneInOtherNotIn(matrixes, numbers, ecuation) and ("/" not in ecuation and "*" not in ecuation) 
        resolvable = allNumbers or allMatrixNoDiv
        if resolvable:
            return resolvable, "all num/matrix(no div)"
        
        resolvable = True
        #Caso con suma
        if "+" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("+"), matrixes, False)
        if not resolvable:
            return resolvable, "not possible +"
        #Caso con resta
        if "-" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("-"), matrixes, False)
        if not resolvable:
            return resolvable, "not possible -"
        #Caso con división
        if "/" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("/"), matrixes, True)
        if not resolvable:
            return resolvable, "not possible /(Div matrix or Div 0)"
        #Caso con mult escalar
        if "*" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("*"), matrixes, False)
        if not resolvable:
            return resolvable, "not possible *Mult scalar to matrix"
        #Caso mult vectorial
        if "x" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("x"), numbers, False)
        if not resolvable:
            return resolvable, "not possible xMult vect to num"
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