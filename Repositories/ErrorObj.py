
class Error:
    # Atributos: __measuredValue, __realValue
    def __init__(self, __measuredValue = 0.0, __realValue = 0.0):
        self.utilNotNull(__measuredValue, __realValue)
        if self.__measuredValue == None or self.__realValue == None:
            raise ValueError("Error: Objeto incompleto")
    
    # Getters:
    def getMeasuredValue(self):
        return self.__measuredValue
    def getRealValue(self):
        return self.__realValue
    
    # Setters:
    def setMeasuredValue(self, __measuredValue):
        self.__measuredValue = __measuredValue
    def setRealValue(self, __realValue):
        self.__realValue = __realValue

    # Validaciones:
    def utilNotNull(self, __measuredValue, __realValue):
        if __measuredValue == None or __realValue == None:
            raise ValueError("Error: Informacion nula") 
        self.__measuredValue = __measuredValue
        self.__realValue = __realValue
        
