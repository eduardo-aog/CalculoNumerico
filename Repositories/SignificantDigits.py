class SignificantDigits:
    def __init__(self, digit):
        self.__utilValDigit(digit)
        if self.__digit == "No decimal":
            self.__numSignificant = "No tiene cifras significativas"
        else:
            self.__utilCountDigits()

    def __utilCountDigits(self): 
        countSignificant = 0
        countSignificant2 = 0 #Cuenta cifras significativas estilo notacion cientifica
        significant2 = False #Verifica notación cientifica ejemplo(7000, 2000, etc)
        flag = False 
        for i in self.__digit:
            if i == "." or i == "," or i == "-":
                significant2 = False
                continue
            if i == "0":
                flag = True
                countSignificant2 += 1  
                significant2 = True
            if i != "0" and flag:
                flag = False
                significant2 = False
            countSignificant += 1
        if significant2:
            self.__numSignificant = "Cifras significantes: "+str(countSignificant)+" o "+str(countSignificant2)
        else:
            self.__numSignificant = "Cifras significantes: "+str(countSignificant)

    def __utilValDigit(self, digit):
        if digit == None:
            raise ValueError("Error: Objeto incompleto")
        if not self.__utilValSpecialChar(digit):
            raise ValueError("Error: Tipo de dato incorrecto")         
        if self.__utilValNotDecimal(digit):
            self.__digit = "No decimal"
        else:
            self.__digit = digit 

    def __utilValNotDecimal(self, digit):
        for i in digit:
            if i.lower() in "abcdef":
                return True
        return False
    
    def __utilValSpecialChar(self, digit):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in digit:
            if i.lower() in specialChars:
                return False
        return True
        
    def getDigit(self):
        return self.__digit
    
    def getNumSignificant(self):
        return self.__numSignificant