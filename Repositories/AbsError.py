from .ErrorObj import Error as ClassError

class AbsoluteError(ClassError):
    def __init__(self, measuredValue = 0.0, realValue  = 0.0):
        ClassError.__init__(self, measuredValue, realValue)
        self.errorAbs = 0.0
        if self.measuredValue == None or self.realValue == None:
            raise ValueError("Error: Objeto incompleto")

    def calcErrorAbs(self):
        if self.realValue != None or self.measuredValue != None:
            self.errorAbs = abs(self.realValue - self.measuredValue)
            return self.errorAbs
        else:
            raise ValueError("Error: Datos nulos")

