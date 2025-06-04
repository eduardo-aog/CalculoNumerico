import random
import time 

def storeData(archive, arFinal, serialRead):
    t = time.localtime()
    timeFormat = time.strftime("%YYYY-%mm-%d %HH:%MM:%SS", t)
    rand = random.randint(0, 101)
    nameRoute = serialRead+"_"+timeFormat+"_serial"+rand+".txt"

    if archive == None or arFinal == None:
        print("Object-Error: Un objeto es nulo")
        return None

    archive.setOrCreateFiles(nameRoute)
    for i in range(len(arFinal)):
        archive.setOrCreateFiles(nameRoute, arFinal[i], True)