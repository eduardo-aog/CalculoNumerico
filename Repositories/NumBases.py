class NumBases:
    __num = ""
    __base = ""

    def __init__(self, num):
        self.__utilValNum(num)
        self.__utilValBase(num)

    def __utilValNum(self, num):
        if num == None:
            raise ValueError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise ValueError("Valor negativo con formato no permitido")
        if "," in num:
            num = self.__utilReplaceCommaFraction(num)
        if not self.__utilValFractionFormat(num):
            raise ValueError("Valor de fracción con formato no permitido")
        if not self.__utilValSpecialChar(num):
            raise ValueError("Valor no permitido, no es un número")
        self.__num = num

    def __utilValBase(self, num):
        base = ""
        base = self.__utilValHex(num, base)
        base = self.__utilValDec(num, base)
        base = self.__utilValBin(num, base)
        if base == "":
            raise ValueError("Valor no permitido, no es un número")
        self.__base = base

    def __utilValBin(self, num, base):
        for i in num:
            if i not in "01":
                return base
        return "Binario/"+base

    def __utilValDec(self, num, base):
        for i in num:
            if i not in "-,.0123456789":
                return base
        return "Decimal/"+base

    def __utilValHex(self, num, base):
        for i in num:
            if i not in "0123456789ABCDEFabcdef":
                return base
        return "Hexadecimal/"+base

    def __utilValNegativeFormat(self, num):
        n = 0
        for i in num:
            if "-" in num and (n == 0 and i!= "-"):
                return False
            if i == "-":
                return True
            n += 1
        return True

    def __utilValFractionFormat(self, num):
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
    
    def __utilValSpecialChar(self, num):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in num:
            if i.lower() in specialChars:
                return False
        return True
    
    def __utilReplaceCommaFraction(self, digit):
        commaless = digit.split(",")
        return commaless[0]+"."+commaless[1]

    def getNum(self):
        return self.__num

    def getBase(self):
        return self.__base