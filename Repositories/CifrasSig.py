class CifrasSig:
    def __init__(self, cifra = ""):
        self.cifra = self.validarCifra(cifra)
        self.contarCifras()

    def contarCifras(self): 
        significante = False
        contador = 0  
        for i in self.cifra:
            if i != "0" and i != ".": 
                significante = True
            if significante == True:
                if i == ".":
                    continue
                contador += 1
        print(contador)

    def validarCifra(self, cifra):
        if cifra == None:
            raise ValueError("Error: Objeto incompleto")
        if type(cifra) != str:
            raise ValueError("Error: Tipo de dato incorrecto")
        return cifra.replace(" ", "")

#Cifra = CifrasSig()
            




