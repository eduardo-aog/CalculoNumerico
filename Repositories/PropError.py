from .AbsError import AbsoluteError

class PropagationError(AbsoluteError):
    def __init__(self,realValue):
        if realValue is None:
            raise ValueError("Error: Objeto incompleto")
        self.realValue = realValue
        self.propagatedValue = self.propagateValue()
        super().__init__(self.propagatedValue, realValue)
        
    def propagateValue(self):
        return self.realValue + 0.1 - 0.3
