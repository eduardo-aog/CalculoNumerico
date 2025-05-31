from .ErrorObj import Error as ClassError

class RelativeError(ClassError):
    def __init__(self, measuredValue=0, realValue=0):
        ClassError.__init__(self, measuredValue, realValue)
        self.relaviteError = 0.0
        if self.measuredValue == None or self.realValue == None:
            raise ValueError("Error: Objeto incompleto")

    def calcErrorRel(self):
        if self.realValue != None or self.measuredValue != None:
            self.relaviteError = abs((self.realValue - self.measuredValue) / self.realValue)
            return self.relaviteError
        else:
            raise ValueError("Error: Datos nulos")
        
