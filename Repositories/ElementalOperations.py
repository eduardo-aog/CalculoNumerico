class ElementalOperations:
    __num = ""
    __op = ""

    def __init__(self, num):
        self.__utilValNum(num)
        self.__utilValOp(num)

    def __utilValNum(self, num):
        if num == None:
            raise AttributeError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise AttributeError("Valor negativo con formato no permitido")
        if not self.__utilValFracFormat(num):
            raise AttributeError("Valor de fracción con formato no permitido")
        self.__num = num

    def __utilValOp(self, num):
        op = ""
        op = self.__utilOpDec(num, op)
        op = self.__utilOpBin(num, op)
        op = self.__utilOpHex(num, op)
        if op == "":
            raise AttributeError("Valor no permitido, no es un número")
        self.__op = op

    def __utilOpBin(self, num, op):
        for i in num:
            if i not in "01":
                return op
        return "+, -, *, /, and, or, not, ^, '+'"

    def __utilOpDec(self, num, op):
        for i in num:
            if i not in "0123456789":
                return op
        return "+, -, *, /, ^, '+'"

    def __utilOpHex(self, num, op):
        for i in num:
            if i not in "0123456789ABCDEFabcdef":
                return op
        return "+, -, *, /, '+'"

    def __utilValNegativeFormat(self, num):
        n = 0
        for i in num:
            if "-" in num and (n == 0 and i!= "-"):
                return False
            if i == "-":
                return True
            n += 1
        return True

    def __utilValFracFormat(self, num):
        n = 0
        for i in num:
            if "," in num and (n == 0 and i == ","):
                return False
            elif "." in num and (n == 0 and i == "."):
                return False
            if ("," in num and "-" in num) and (n == 1 and i == ","):
                return False
            elif ("." in num and "-" in num) and (n == 1 and i == "."):
                return False
            if i == "," or i == ".":
                return True
            n += 1
        return True

    def getNum(self):
        return self.__num

    def getOperation(self):
        return self.__op