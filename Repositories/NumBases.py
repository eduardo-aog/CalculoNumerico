class NumBases:
    __num = ""
    __base = ""

    def __init__(self, num:str):
        self.__utilValNum(num)
        self.__utilBases(num)

    def __utilValNum(self, num:str):
        if num == None:
            raise ValueError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise ValueError("Valor negativo con formato no permitido")
        num = self.__utilReplaceCommaFraction(num)
        if not self.__utilValFractionFormat(num):
            raise ValueError("Valor de fracción con formato no permitido")
        if not self.__utilValSpecialChar(num):
            raise ValueError("Valor no permitido, no es un número")
        self.__num = num

    def __utilBases(self, num:str):
        base = ""
        base = self.__utilHexInNumber(num, base)
        base = self.__utilDecInNumber(num, base)
        base = self.__utilBinInNumber(num, base)
        if base == "":
            raise ValueError("Valor no permitido, no es un número")
        self.__base = base

    def __valNumsAllowed(numStr:str, stringValuesAllowed:str) -> bool:
        if numStr==None:
            return False
        for i in numStr:
            if i not in stringValuesAllowed:
                return False
        return True

    def __utilBinInNumber(self, num:str, base:str) -> str:
        if not self.__valNumsAllowed(num, "01"):
            return base
        return "Binario/"+base

    def __utilDecInNumber(self, num:str, base:str) -> str:
        if not self.__valNumsAllowed(num, "-.0123456789"):
            return base
        return "Decimal/"+base

    def __utilHexInNumber(self, num:str, base:str) -> str:
        if not self.__valNumsAllowed(num, "0123456789ABCDEFabcdef"):
            return base
        return "Hexadecimal/"+base

    def __utilValNegativeFormat(self, num:str) -> bool:
        n = 0
        for i in num:
            if "-" in num and (n == 0 and i!= "-"):
                return False
            if i == "-":
                return True
            n += 1
        return True

    def __utilValFractionFormat(self, num:str) -> bool:
        n = 0
        for i in num:
            if "." in num and (n == 0 and i == "."):
                return False
            if ("." in num and "-" in num) and (n == 1 and i == "."):
                return False
            if i == ".":
                return True
            n += 1
        return True
    
    def __utilValSpecialChar(self, num:str) -> bool:
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in num:
            if i.lower() in specialChars:
                return False
        return True
    
    def __utilReplaceCommaFraction(self, num:str) -> str:
        if "," in num:
            commaless = num.split(",")
            return commaless[0]+"."+commaless[1]
        return num

    def getNum(self):
        return self.__num

    def getBase(self):
        return self.__base