import random as rm
import time as tm
        
def nombreArchivo():
    serial1 = str(rm.randint(10,99))
    fecha = tm.strftime("%Y/%m/%d") 
    serial2 = str(rm.randint(10,99))
    return serial1 + "_" + fecha + "_" + serial2

    
        