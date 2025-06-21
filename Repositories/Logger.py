import time 
import os
    
def storeArchiveLog(error):
    try:
        with open(os.path.dirname(os.path.abspath(__file__))+os.path.sep+"Errors.log", "a") as logger:
            logger.write(f"!!Error!!: {__validateError(error)} ({time.strftime("%Y/%m/%d_%H:%M")})\n")
    except FileNotFoundError:
        print("Error: Archivo Logger no encontrado")

def __validateError(error):
    if type(error) != str:
        storeArchiveLog("Tipo de dato incorrecto")
    return error