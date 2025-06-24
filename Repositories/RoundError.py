from .AbsError import AbsoluteError

class RoundError(AbsoluteError):
    def __init__(self, realValue):
        if realValue is None:
            raise ValueError("Error: Objeto incompleto")
        self.roundedValue = round(realValue)
        super().__init__(self.roundedValue, realValue)

