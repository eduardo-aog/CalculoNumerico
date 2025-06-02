class ElementalOperations:
    __num = ""
    __op = ""

    def __init__(self, num):
        self.__utilValNum(num)
        self.__utilValOp(num)

    def __utilValNum(self, num):
        if num == None:
            raise AttributeError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise AttributeError("Valor negativo con formato no permitido")
        if not self.__utilValFractionFormat(num):
            raise AttributeError("Valor de fracción con formato no permitido")
        self.__num = num

    def __utilValOp(self, num):
        op = ""
        op = self.__utilOpDec(num, op)
        op = self.__utilOpBin(num, op)
        op = self.__utilOpHex(num, op)
        if op == "":
            raise AttributeError("Valor no permitido, no es un número")
        self.__op = op

    def __utilOpBin(self, num, op):
        for i in num:
            if i not in "01":
                return op
            if self.__utilCheckSpecialChar(i):
                return ""
        res = self.__utilBinToDec(num)
        if not self.__utilCheckSum(res):
            return ""
        
        return "+, -, *, /, ^, ''+''"

    def __utilOpDec(self, num, op):
        for i in num:
            if i not in "-,.0123456789":
                return op
            if self.__utilCheckSpecialChar(i):
                return ""
        if not self.__utilCheckSum(num):
            return ""   
        
        return "+, -, *, /, ^, ''+''"

    def __utilOpHex(self, num, op):
        for i in num:
            if i.lower() not in "0123456789abcdef":
                return op
            if self.__utilCheckSpecialChar(i):
                return ""
        res = self.__utilHexToDec(num)
        if not self.__utilCheckSum(res):
            return ""

        return "+, -, *, /, ^, ''+''"
    
    def __utilCheckSpecialChar(n):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨*"
        if n.lower() in specialChars:
            return True
        return False
    
    def __utilXorGate(a, b):
        if (a or b) and not(a and b):
            return True
        return False
    
    def __utilBinSum(self, num1, num2):
        sum = ""
        carry = "0"
        if len(num2) < len(num1):
            for i in range(len(num1)-len(num2)):
                num2 = "0" + num2
        elif len(num2) > len(num1):
            for i in range(len(num2)-len(num1)):
                num1 = "0" + num1
        
        for i in range(len(num1)):
            lastToFirst = len(num1)-1-i
            if self.__utilXorGate(num1[lastToFirst]=="1", num2[lastToFirst]=="1") and carry=="0":
                sum = "1" + sum
            elif not self.__utilXorGate(num1[lastToFirst]=="1", num2[lastToFirst]=="1") and carry=="1":
                sum = "1" + sum
            else:
                sum = "0" + sum
            if num1[lastToFirst]=="1" and num2[lastToFirst]=="1":
                carry = "1"
            elif self.__utilXorGate(num1[lastToFirst]=="1", num2[lastToFirst]=="1") and carry =="1":
                carry = "1"
            else:
                carry = "0"
        return sum

    def __utilBinToDec(num):
        n = 0
        comp = 0
        for i in reversed(num):
            comp += 2**n * int(i)
            n += 1
        return comp
    
    def __utilHexToDec(num):
        n = 0
        comp = 0
        hexa = "0123456789abcdef"
        for i in reversed(num):
            for j in range(len(hexa)):
                if i.lower() == hexa[j]:
                    comp += 16**n * j
            n += 1
        return comp
    
    def __utilCheckSum(num): #Creo que puede arrojar ValueError
        test = float(num) + 10 
        if type(test) == float:
            return True
        return False

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

    def getNum(self):
        return self.__num

    def getOperation(self):
        return self.__op