import random as rm
import time as tm
class Archivo:
    def __init__(self):
        self.serial1 = ""
        self.fecha = ""
        self.serial2 = ""
        self.nombreArchivo()
        
    def nombreArchivo(self):
        self.serial1 = str(rm.randint(10,99))
        self.fecha = tm.strftime("%Y/%m/%d_%H:%M") 
        self.serial2 = str(rm.randint(10,99))
        
        
Obj = Archivo()
print(Obj.serial1 + "_" + Obj.fecha + "_" + Obj.serial2)