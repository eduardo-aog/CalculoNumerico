class CifrasSig:
    def __init__(self, cifra = ""):
        self.cifra = self.validarCifra(cifra)
        if self.cifra == "No decimal":
            print("No tiene cifras significativas")
            return
        self.contarCifras()

    def contarCifras(self): 
        significante = False
        contador = 0  
        for i in self.cifra:
            if i != "0" and i != ".": 
                significante = True
            if significante == True:
                if i == "." or i == ",":
                    continue
                contador += 1
        print(contador)

    def validarCifra(self, cifra):
        if cifra == None:
            raise ValueError("Error: Objeto incompleto")
        if type(cifra) != str:
            raise ValueError("Error: Tipo de dato incorrecto")
        decimal = True
        for i in cifra:
            if i in "ABCDEFabcdef":
                decimal = False
            if i in "GHIJKLMNOPQRSTUVWXYZÑghijklmnopqrstuvwxyzñ":
                raise ValueError("Error: Tipo de dato incorrecto")
        if decimal:
            return cifra.replace(" ", "")
        else:
            return "No decimal"

            




