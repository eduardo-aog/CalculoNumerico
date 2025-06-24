import time 
import random
import os

class Logger:    
    def storeArchiveLog(self, error:str):
        try:
            with open(os.path.dirname(os.path.abspath("Main.py"))+os.path.sep+"archivo.log", "a") as logger:
                logger.write(f"ErrorSystemValues_{time.strftime("%Y/%m/%d_%H:%M")}_serial{random.randint(0,101)} Error:[{error}] \n")
        except FileNotFoundError as e:
            print(f"Error: Archivo Logger no encontrado: {e}")