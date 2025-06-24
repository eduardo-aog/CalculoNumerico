class CheckEcuationResolvable:
    def __init__(self, ecuation):
        self.__utilValEcuationFormat(ecuation)
        self.__utilResolvable()
    #UN PARENTESIS
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
    
    def __countOperator(self, ecuation, operators):
        count = 0
        for value in ecuation:
            for n in operators:
                if value == n:
                    count += 1
        return count  
    
    def __separateBracketsProcess(self, ecuation):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        outsideBracket = ""
        for i in range(len(ecuation.split("("))-1):
            if self.__countOperator(ecuation, matrixes)>0:
                openBracket = ecuation.split("(")
                openBracket1 = openBracket[i+1]
                outsideBracket1 = openBracket[i]
                closedBracket = openBracket1.split(")")
                insideBrackets = closedBracket[i]
                outsideBracket = outsideBracket+outsideBracket1+"A"+closedBracket[i]
            else:
                openBracket = ecuation.split("(")
                openBracket = openBracket[i+1]
                outsideBracket1 = openBracket[i]
                closedBracket = openBracket.split(")")
                insideBrackets = closedBracket[i]
                outsideBracket = outsideBracket1+"1"+closedBracket[i+1]
        return insideBrackets, outsideBracket
    
    def __isItResolvable(self):
        if '(' in self.__ecuation:
            numberBrackets = self.__countOperator(self.__ecuation, "(")
            for i in range(numberBrackets):
                if i==0:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(self.__ecuation)              
                    resolvable, reason = self.__isEcuationResolvableProcess(insideBrackets)
                    if not resolvable:
                        return resolvable, reason
                else:
                    insideBrackets, outsideBracket = self.__separateBracketsProcess(outsideBracket)          
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
        #Caso con división
        if "/" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("/"), matrixes, True)
        if not resolvable:
            return resolvable, "not possible /(Div matrix or Div 0)"
        #Caso con mult escalar
        if "*" in ecuation:
            resolvable = not self.__checkLettersInOperator(ecuation.split("*"), matrixes, False)
            ecuation = self.__orderScalarMult(ecuation)
            print(ecuation)
        if not resolvable:
            return resolvable, "not possible *Mult scalar to matrix"
        #Caso mult vectorial
        if "x" in ecuation:
            resolvable = self.__checkLettersInOperator(ecuation.split("x"), numbers, False)
        if not resolvable:
            return resolvable, "not possible xMult vect to num"
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

        return resolvable, "is possible"
    
    def __orderScalarMult(self, ecuation):
        band = True
        ecuationContainer = ""
        for i in range(len(ecuation.split("*"))-1):
            band = False
            side = self.__whichSideMatrix(ecuation.split("*")[i], ecuation.split("*")[i+1])
            if side=="L":
                withoutLast = self.__removeLastOrFisrt(ecuation.split("*")[i], False)
                ecuationContainer = ecuationContainer+withoutLast+"A"
            elif side=="R":
                withoutFirst = self.__removeLastOrFisrt(ecuation.split("*")[i], True)
                ecuationContainer = ecuationContainer+withoutFirst+"A"
        if band:
            side = self.__whichSideMatrix(ecuation.split("*")[0], ecuation.split("*")[1])
            withoutLast = self.__removeLastOrFisrt(ecuation.split("*")[0], True)
            withoutFirst = self.__removeLastOrFisrt(ecuation.split("*")[1], False)

            ecuationContainer = withoutLast+"A"+withoutFirst
        return ecuationContainer
    
    def __whichSideMatrix(self, firstValue, secondValue):
        matrixes = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"            
        isBeforeOperatorLetter = firstValue in matrixes
        isAfterOperatorLetter = secondValue in matrixes
        if isBeforeOperatorLetter and not isAfterOperatorLetter: 
            return "L"
        elif not isBeforeOperatorLetter and isAfterOperatorLetter:
            return "R"
    
    def __removeLastOrFisrt(self, string, last):
        newStr = ""
        if last:
            for i in range(len(string)-1):
                newStr = newStr+string[i]
            return newStr
        else:
            for i in range(len(string)-1):
                newStr = newStr+string[i+1]
        return newStr

    def __checkSpecialChars(self, ecuation):
        specialChars = "|°¬!#$%&?¡¿´;:_¨ "
        for i in ecuation:
            if i in specialChars:
                return False
        return True

    def getEcuation(self):
        return self.__ecuation
    
    def getResolvable(self):
        return self.__resolvable
    
    def getCientificNotation(self):
        return self.__cientificNotation