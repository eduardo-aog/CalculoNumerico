import time 
import random
import os

class Logger:    
    def storeArchiveLog(self, error):
        try:
            with open(os.path.dirname(os.path.abspath("Main.py"))+os.path.sep+"Errors.log", "a") as logger:
                logger.write(f"ErrorSystemValues_{time.strftime("%Y/%m/%d_%H:%M")}_serial{random.randint(0,101)} Error:[{self.__validateError(error)}] \n")
        except FileNotFoundError as e:
            print(f"Error: Archivo Logger no encontrado: {e}")

    def __validateError(self, error):
        if type(error) != str:
            self.storeArchiveLog("Tipo de dato incorrecto")
        return error