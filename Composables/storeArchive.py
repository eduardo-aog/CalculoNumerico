import random
import time 

def storeData(archive, arFinal, serialRead):
    t = time.localtime()
    timeFormat = time.strftime("%Y-%m-%d--%H-%M-%S", t)
    rand = random.randint(0, 101)
    nameRoute = serialRead+"_"+timeFormat+"_serial"+str(rand)+".txt"

    if archive == None or arFinal.any == None:
        print("Object-Error: Un objeto es nulo")
        return None

    for i in range(len(arFinal)):
        archive.setOrCreateFiles(nameRoute, arFinal[i], i<len(arFinal)-1)