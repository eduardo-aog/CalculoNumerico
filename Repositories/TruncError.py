from .AbsError import AbsoluteError
from math import factorial

class TruncError(AbsoluteError):
    def __init__(self, realValue):
        if realValue is None:
            raise ValueError("Error: Objeto incompleto")
        self.realValue = realValue
        self.truncatedValue = self.truncateValue(3) 
        super().__init__(self.truncatedValue, realValue)
    
    def truncateValue(self, n):
        if self.realValue is not None:
            sum = 0.0
            for i in range(n):
                sum += (-1)**i * (self.realValue / factorial(2*i))
            return sum
        else:
            raise ValueError("Error: Datos nulos")

