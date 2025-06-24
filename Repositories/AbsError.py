from .ErrorObj import Error as ClassError

class AbsoluteError(ClassError):
    def __init__(self, measuredValue, realValue):
        super().__init__(measuredValue, realValue)
        self.measuredValue = self.getMeasuredValue()
        self.realValue = self.getRealValue()
        self.absoluteError = 0.0
        if self.measuredValue is None or self.realValue is None:
            raise ValueError("Error: Objeto incompleto")

    def calcErrorAbs(self):
        if self.realValue is not None and self.measuredValue is not None:
            self.absoluteError = abs(self.realValue - self.measuredValue)
            return self.absoluteError
        else:
            raise ValueError("Error: Datos nulos")

