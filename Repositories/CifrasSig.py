import numpy #Agregado ya que se está trabajndo con Numpy si no da error

class CifrasSig:
    def __init__(self, digit):
        self.__utilValDigit(digit)
        if self.__digit == "No decimal":
            self.__numSignificant = "No tiene cifras significativas"
        else:
            self.__utilCountDigits()

    def __utilCountDigits(self): 
        countSignificant = 0  
        for i in self.__digit:
            significant = False
            if i != "0" and (i != "." and i != ",") and i != "-": 
                significant = True
            if significant == True:
                countSignificant += 1
        self.__numSignificant = countSignificant

    def __utilValDigit(self, digit):
        if digit == None:
            raise ValueError("Error: Objeto incompleto")
        if type(digit) != str or type(digit) != numpy.str_:
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