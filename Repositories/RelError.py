from .ErrorObj import Error as ClassError

class RelativeError(ClassError):
    def __init__(self, measuredValue, realValue):
        super().__init__(measuredValue, realValue)
        self.measuredValue = self.getMeasuredValue()
        self.realValue = self.getRealValue()
        self.relativeError = 0.0
        if self.measuredValue is None or self.realValue is None:
            raise ValueError("Error: Objeto incompleto")

    def calcErrorRel(self):
        if self.realValue is not None and self.measuredValue is not None:
            self.relativeError = abs((self.realValue - self.measuredValue) / self.realValue)
            return self.relativeError
        else:
            raise ValueError("Error: Datos nulos")