import numpy #Agregado ya que se está trabajndo con Numpy si no da error

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
        significant = False
        significant2 = True #Verifica notación cientifica ejemplo(7000, 2000, etc)
        flag = False #Verificar notación cientifica x2  
        for i in self.__digit:
            if i != "0" and i != "." and i != "," and i != "-": 
                significant = True
            if significant == True:
                if i == "." or i == "," or i == "-":
                    significant2 = False
                    continue
                if i == "0":
                    flag = True
                if i != "0" and flag == False:
                    countSignificant2 += 1  
                countSignificant += 1
                if i != "0" and flag == True:
                    significant2 = False
            else:
                if i != "0":
                    significant2 = False
        self.__numSignificant = countSignificant
        if significant == True and significant2 == True:
            print(f"Cifras significantes: {self.__numSignificant} o {countSignificant2}")
        elif significant == True:
            print(f"Cifras significantes: {self.__numSignificant}")
        else:
            print("No hay cifras significativas")

        countSignificant = 0  
        for i in self.__digit:
            significant = False
            if i != "0" and (i != "." and i != ",") and i != "-": 
                significant = True
            if significant == True:
                countSignificant += 1
        self.__numSignificant = countSignificant
>

    def __utilValDigit(self, digit):
        if digit == None:
            raise ValueError("Error: Objeto incompleto")
        if type(digit) != str and type(digit) != numpy.str_:
            raise ValueError("Error: Tipo de dato incorrecto")
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