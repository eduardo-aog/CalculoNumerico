import time 
import random
import os
    
def storeArchiveLog(error):
    try:
        with open(os.path.dirname(os.path.abspath("Main.py"))+os.path.sep+"Errors.log", "a") as logger:
            logger.write(f"ErrorSystemValues_{time.strftime("%Y/%m/%d_%H:%M")}_serial{random.randint(0,101)} Error:[{__validateError(error)}] \n")
    except FileNotFoundError:
        print("Error: Archivo Logger no encontrado")

def __validateError(error):
    if type(error) != str:
        storeArchiveLog("Tipo de dato incorrecto")
    return error