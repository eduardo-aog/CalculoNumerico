class BasesConversion:
    __num = ""
    __bases = ""
    __numBase2 = ""
    __numBase10 = ""
    __numBase16 = ""

    def __init__(self, num, bases):
        self.__utilValNum(num)
        self.__utilValBases(num)
        self.__utilValConversion(num, bases)

    def __utilValNum(self, num):
        if num == None:
            raise AttributeError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise AttributeError("Valor negativo con formato no permitido")
        if not self.__utilValFractionFormat(num):
            raise AttributeError("Valor de fracción con formato no permitido")
        if not self.__utilValSpecialChar(num):
            raise AttributeError("Valor no permitido, no es un número")
        self.__num = num

    def __utilValBases(self, bases):
        if bases == None:
            raise AttributeError("Valor nulo no permitido")
        if not self.__utilValFormatBases(bases):
            raise AttributeError("Formato no permitido para las bases")
        
        self.__bases = bases

    def __utilValConversion(self, num, bases):
        if "Binario" in bases:
            self.__numBase2 = num
            self.__numBase10 = self.__utilBinToDecimal(num)
            self.__numBase16 = self.__utilDecimalToHex(self.__numBase10)
        elif "Decimal" in bases and "Hexadecimal" in bases:
            return 1
        elif "Hexadecimal" in bases:
            self.__numBase16 = num
            self.__numBase10 = self.__utilHexToDecimal(num)
            self.__numBase2 = self.__utilDecimalToBin(self.__numBase10)
        else:
            self.__numBase10 = num
            self.__numBase16 = self.__utilDecimalToHex(num)
            self.__numBase2 = self.__utilDecimalToBin(num)
        
    def __utilBinToDecimal(self, num):
        dec = 0
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            if num[lastToFirst]!="0":
                dec = 2**i + dec
        return dec
    
    def __utilDecimalToHex(self, num):
        hex = "0123456789abcdef"
        hexConversion = ""
        for i in range(len(num)):
            remainder = num%16
            num /= 16
            if num[i]=="." or num[i]==",":
                break
            for j in range(16):
                if j == remainder:
                    hexConversion = hex[j] + hexConversion           
        if num<0:
            hexConversion = "-" + hexConversion
        return hexConversion
            
    def __utilDecimalToBin(self, num):
        bin = ""
        for i in range(len(num)):
            remainder = num%2
            num /= 2
            if num[i]=="." or num[i]==",":
                break
            if remainder==1:
                bin = "1" + bin
            else:
                bin = "0" + bin           
        if num<0:
            bin = "-" + bin       
        return bin

    def __utilHexToDecimal(self, num):
        hex = "0123456789abcdef"
        decimal = ""
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            for j in range(len(hex)):
                if hex[j].lower==num[lastToFirst]:
                    decimal = j*16**i + decimal
        return decimal

    def __utilValFormatBases(self, bases):
        if "/" not in bases:
            return False
        separateBases = bases.split("/")
        for i in separateBases:
            if i!="Binario" or i!="Decimal" or i!="Hexadecimal":
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
            if "," in num and (n == 0 and i == ","):
                return False
            elif "." in num and (n == 0 and i == "."):
                return False
            if ("," in num and "-" in num) and (n == 1 and i == ","):
                return False
            elif ("." in num and "-" in num) and (n == 1 and i == "."):
                return False
            if i == "," or i == ".":
                return True
            n += 1
        return True
    
    def __utilValSpecialChar(self, num):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in num:
            if i.lower() in specialChars:
                return False
        return True

    def getNum(self):
        return self.__num

    def getBases(self):
        return self.__bases