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
        if not self.__utilValSpecialChar(num):
            raise AttributeError("Valor no permitido, no es un número")
        self.__num = num

    def __utilValOp(self, num):
        op = ""
        op = self.__utilOpHex(num, op)
        op = self.__utilOpDec(num, op)
        op = self.__utilOpBin(num, op)
        if op == "":
            raise AttributeError("Valor no permitido, no es un número")
        self.__op = op

    def __utilOpBin(self, num, op):
        for i in num:
            if i not in "01":
                return op
        sum = self.__utilBinSum(num, num)
        minus = self.__utilBinMinus(num, num)
        product = self.__utilBinMult(num, "10")
        div = self.__utilBinDiv(num, "10")
        
        return "+, -, *, /, +(Concatenacion)"

    def __utilOpDec(self, num, op):
        for i in num:
            if i not in "-,.0123456789":
                return op
        if not self.__utilDecSum(num, num):
            return ""   
        if not self.__utilDecMinus(num, num):
            return ""
        if not self.__utilDecMult(num, "2"):
            return ""
        if not self.__utilDecDiv(num, "2"):
            return ""
        
        return "+, -, *, /, +(Concatenacion)"

    def __utilOpHex(self, num, op):
        for i in num:
            if i.lower() not in "0123456789abcdef":
                return op

        return "+(Concatenacion)"
    
    def __utilTrueOneButNotBoth(self, a, b):
        if (a or b) and not(a and b):
            return True
        return False
    
    def __utilLargerNumber(self, num1, num2):
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
            bin1 = num1[lastToFirst]=="1"
            bin2 = num2[lastToFirst]=="1"
            if self.__utilTrueOneButNotBoth(bin1, bin2) and carry=="0":
                sum = "1" + sum
            elif not self.__utilTrueOneButNotBoth(bin1, bin2) and carry=="1":
                sum = "1" + sum
            else:
                sum = "0" + sum
            if bin1 and bin2:
                carry = "1"
            elif self.__utilTrueOneButNotBoth(bin1, bin2) and carry =="1":
                carry = "1"
            else:
                carry = "0"
                
        if carry=="1":
            sum = "1" + sum 

        return sum, carry
    
    def __utilComplement1(self, num):
        inverseValue = ""
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            if num[lastToFirst]=="1":
                inverseValue = "0" + inverseValue
            elif num[lastToFirst]=="0":
                inverseValue = "1" + inverseValue
        return inverseValue
                
    def __utilBinMinus(self, num1, num2):
        inverseValue = ""
        minus = ""
        carry = "0"

        num2 = self.__utilLargerNumber(num1, num2)
        num1 = self.__utilLargerNumber(num2, num1) 

        inverseValue = self.__utilComplement1(num2)
        minus, carry = self.__utilBinSum(num1, inverseValue)
        if carry=="1":
            minus = self.__utilBinSum(minus, carry)
        else:
            minus = "-" + minus
        
        return minus
    
    def __utilBinMult(self, num1, num2):
        product = ""
        mult = num1

        for i in range(len(num2)):
            lastToFirst = len(num2)-1-i
            if num2[lastToFirst]=="1" and i!=0:
                product = self.__utilBinSum(num1, mult)[0] + product
                mult = mult + "0"
            else:
                mult = mult + "0"
        
        return product

    def __utilBinDiv(self, num1, num2):
        digsForOperation = ""
        result = ""
        carry = ""

        if num2!="0":
            for i in range(len(num1)):
                if len(digsForOperation)<len(num2):
                    digsForOperation = digsForOperation + num1[i]
                    if result!="":
                        result = result + "0"
                else:
                    carry = self.__utilBinMinus(digsForOperation, num2)
                if carry=="1" or digsForOperation==num2:
                    result = result + "1"
                    if digsForOperation==num2:
                        carry = ""
                elif carry=="0":
                    result = result + "0"
                    carry = ""
                digsForOperation = carry

        return result   
                
    #Pueden arrojar ValueError las op decimales
    def __utilDecSum(self, num1, num2): 
        test = str(float(num1) + float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecMinus(self, num1, num2):
        test = str(float(num1) - float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecMult(self, num1, num2):
        test = str(float(num1) * float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecDiv(self, num1, num2):
        if float(num2)!=0:
            test = str(float(num1) / float(num2)) 
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
    
    def __utilValSpecialChar(self, num):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in num:
            if i.lower() in specialChars:
                return False
        return True

    def getNum(self):
        return self.__num

    def getOperation(self):
        return self.__op