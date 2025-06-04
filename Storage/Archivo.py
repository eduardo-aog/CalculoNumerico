import random as rm
import time as tm
        
def nombreArchivo():
    serial1 = str(rm.randint(10,99))
    fecha = tm.strftime("%Y/%m/%d_%H:%M")
    serial2 = str(rm.randint(10,99))
    return serial1 + "_" + fecha + "_" + serial2

def archivo_log(error):
    with open("Archivo.log", "a", encoding = "utf-8") as archivo:
        archivo.write(f"!!Error!!: {validarError(error)} ({tm.strftime("%Y/%m/%d_%H:%M")})\n")

def validarError(error):
    if type(error) != str:
        archivo_log("Tipo de dato incorrecto")
    return error
