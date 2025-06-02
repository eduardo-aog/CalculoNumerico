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
        sum = self.__utilBinSum(num, num)
        for i in sum:
            if i not in "01":
                return ""
        
        return "+, -, *, /, ^, ''+''"

    def __utilOpDec(self, num, op):
        for i in num:
            if i not in "-,.0123456789":
                return op
            if self.__utilCheckSpecialChar(i):
                return ""
        if not self.__utilDecSum(num, num):
            return ""   
        
        return "+, -, *, /, ^, ''+''"

    def __utilOpHex(self, num, op):
        for i in num:
            if i.lower() not in "0123456789abcdef":
                return op
            if self.__utilCheckSpecialChar(i):
                return ""
        sum = self.__utilHexSum(num, num)
        for i in sum:
            if i.lower() not in "0123456789abcdef":
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
    
    def __utilLargerNumber(num1, num2):
        if len(num2) < len(num1):
            for i in range(len(num1)-len(num2)):
                num2 = "0" + num2
        return num2
    
    def __utilBinSum(self, num1, num2):
        sum = ""
        carry = "0"

        num2 = self.__utilLargerNumber(num1, num2)
        num1 = self.__utilLargerNumber(num2, num1)       
        
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
                
        if carry=="1":
            sum = "1" + sum 

        return sum
    
    def __utilHexToPosition(num):
        hexa = "0123456789abcdef"
        for j in range(len(hexa)):
            if num.lower() == hexa[j]:
                return j
        return 0
    
    def __utilPositionToHex(pos):
        hexa = "0123456789abcdef"
        for j in range(len(hexa)):
            if pos == j:
                return hexa[j]
        return 0
    
    def __utilHexSum(self, num1, num2):
        sum = ""
        carry = "0"    

        num2 = self.__utilLargerNumber(num1, num2)
        num1 = self.__utilLargerNumber(num2, num1) 

        for i in range(len(num1)):
            lastToFirst = len(num1)-1-i
            positionNum1 = self.__utilHexToPosition(num1[lastToFirst])
            positionNum2 = self.__utilHexToPosition(num2[lastToFirst])
            if carry=="1":
                positionNum1 += 1
            if (positionNum1 + positionNum2) >= 16:
                positionSum = self.__utilPositionToHex((positionNum1 + positionNum2)-16)
                carry = "1"
            else:
                positionSum = self.__utilPositionToHex((positionNum1 + positionNum2))
                carry = "0"

            sum = positionSum + sum
            
        if carry=="1":
            sum = "1" + sum    

        return sum

    
    def __utilDecSum(num1, num2): #Puede arrojar ValueError
        test = str(float(num1) + float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
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

    def getNum(self):
        return self.__num

    def getOperation(self):
        return self.__op