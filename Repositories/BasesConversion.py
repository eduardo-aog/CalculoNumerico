class BasesConversion: 
    __num = ""
    __bases = ""
    __numBase2 = ""
    __numBase10 = ""
    __numBase16 = ""

    def __init__(self, num, bases):
        self.__utilValNum(num)
        self.__utilValBases(bases)
        self.__utilValConversion()

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

    def __utilValBases(self, bases):
        if bases == None:
            raise ValueError("Valor nulo no permitido")
        if not self.__utilValFormatBases(bases):
            raise ValueError("Formato no permitido para las bases")
        
        self.__bases = bases

    def __utilValConversion(self):
        separateBases = self.__bases.split("/")
        if "Binario"==separateBases[0]:
            self.__numBase2 = self.__utilBinToDecimal(self.__num)
            self.__numBase10 = self.__num
            self.__numBase16 = self.__utilHexToDecimal(self.__num)
        elif "Decimal"==separateBases[0] and "Hexadecimal"==separateBases[1]:
            self.__numBase2 = "No puede ser tomado como Binario"
            self.__numBase10 = self.__num
            self.__numBase16 = self.__utilHexToDecimal(self.__num)
        elif "Hexadecimal"==separateBases[0]:
            self.__numBase2 = "No puede ser tomado como Binario"
            self.__numBase10 = "No puede ser tomado como Decimal"
            self.__numBase16 = self.__utilHexToDecimal(self.__num)
        else:
            self.__numBase2 = "No puede ser tomado como Binario"
            self.__numBase10 = self.__num
            self.__numBase16 = "No puede ser tomado como Hexadecimal"        
        
    def __utilBinToDecimal(self, num):
        dec = 0
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            if num[lastToFirst]!="0":
                dec = str(2**i) + dec
        return dec

    def __utilHexToDecimal(self, num):
        hex = "0123456789abcdef"
        decimal = ""
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            for j in range(len(hex)):
                if hex[j]==num[lastToFirst]:
                    decimal = str(j*16**i) + decimal
        return decimal

    def __utilValFormatBases(self, bases):
        if "/" not in bases:
            return False
        return True

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

    def getBases(self):
        return self.__bases
    
    def getNumPossiblyBin(self):
        return self.__numBase2
    
    def getNumPossiblyDec(self):
        return self.__numBase10
    
    def getNumPossiblyHex(self):
        return self.__numBase16