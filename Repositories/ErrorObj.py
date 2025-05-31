
class Error:
    def __init__(self, measuredValue, realValue):
        self.utilNotNull(measuredValue, realValue)
        if self.measuredValue == None or self.realValue == None:
            raise ValueError("Error: Objeto incompleto")
        
    # Validaciones:
    def utilNotNull(self, measuredValue, realValue):
        if measuredValue == None or realValue == None:
            raise ValueError("Error: Informacion nula") 
        self.measuredValue = measuredValue
        self.realValue = realValue
    
    
