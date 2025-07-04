class NumBases:
    __numberToAnalize = ""
    __basesAvailables = ""

    def __init__(self, numberToAnalize:str):
        self.__utilValNum(numberToAnalize)
        self.__utilBases(numberToAnalize)

    def __utilValNum(self, numberToAnalize:str):
        if numberToAnalize == None:
            raise ValueError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(numberToAnalize):
            raise ValueError("Valor negativo con formato no permitido")
        numberToAnalize = self.__utilReplaceCommaFraction(numberToAnalize)
        if not self.__utilValFractionFormat(numberToAnalize):
            raise ValueError("Valor de fracción con formato no permitido")
        if not self.__utilValSpecialChar(numberToAnalize):
            raise ValueError("Valor no permitido, no es un número")
        self.__numberToAnalize = numberToAnalize

    def __utilBases(self, numberToAnalize:str):
        basesAvailables = ""
        basesAvailables = self.__utilHexInNumber(numberToAnalize, basesAvailables)
        basesAvailables = self.__utilDecInNumber(numberToAnalize, basesAvailables)
        basesAvailables = self.__utilBinInNumber(numberToAnalize, basesAvailables)
        if basesAvailables == "":
            raise ValueError("Valor no permitido, no es un número")
        self.__basesAvailables = basesAvailables

    def __valNumsAllowed(numStr:str, stringValuesAllowed:str) -> bool:
        if numStr==None:
            raise ValueError("Valor nulo no permitido")
        for i in numStr:
            if i not in stringValuesAllowed:
                return False
        return True

    def __utilBinInNumber(self, numberToAnalize:str, base:str) -> str:
        if not self.__valNumsAllowed(numberToAnalize, "01"):
            return base
        return "Binario/"+base

    def __utilDecInNumber(self, numberToAnalize:str, base:str) -> str:
        if not self.__valNumsAllowed(numberToAnalize, "-.0123456789"):
            return base
        return "Decimal/"+base

    def __utilHexInNumber(self, numberToAnalize:str, base:str) -> str:
        if not self.__valNumsAllowed(numberToAnalize, "0123456789ABCDEFabcdef"):
            return base
        return "Hexadecimal/"+base

    def __utilValNegativeFormat(self, numberToAnalize:str) -> bool:
        n = 0
        for i in numberToAnalize:
            if "-" in numberToAnalize and (n == 0 and i!= "-"):
                return False
            if i == "-":
                return True
            n += 1
        return True

    def __utilValFractionFormat(self, numberToAnalize:str) -> bool:
        n = 0
        for i in numberToAnalize:
            if "." in numberToAnalize and (n == 0 and i == "."):
                return False
            if ("." in numberToAnalize and "-" in numberToAnalize) and (n == 1 and i == "."):
                return False
            if i == ".":
                return True
            n += 1
        return True
    
    def __utilValSpecialChar(self, numberToAnalize:str) -> bool:
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in numberToAnalize:
            if i.lower() in specialChars:
                return False
        return True
    
    def __utilReplaceCommaFraction(self, numberToAnalize:str) -> str:
        if "," in numberToAnalize:
            commaless = numberToAnalize.split(",")
            return commaless[0]+"."+commaless[1]
        return numberToAnalize

    def getNum(self):
        return self.__numberToAnalize

    def getBase(self):
        return self.__basesAvailables