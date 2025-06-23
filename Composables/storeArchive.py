import random
import time 
from Repositories.Logger import storeArchiveLog

def storeData(archive, arFinal, errorPerArchive, archivesNames):
    if archive == None or arFinal.any == None:
        storeArchiveLog("Object-Error: Un objeto es nulo")
        exit()
    
    for m in range(len(arFinal)):
        nameRoute = __storeArchiveFormat(archivesNames[m])
        for i in range(len(arFinal[m])):
            if str(arFinal[m][i]) != "nan":
                archive.setOrCreateFiles(nameRoute, arFinal[m][i], i<len(arFinal[m])-1-errorPerArchive[m])
            else:
                continue

def __storeArchiveFormat(nameArchive):
    timeFormat = time.strftime("%Y-%m-%d--%H-%M-%S", time.localtime())
    serialRead = nameArchive.split("_")[len(nameArchive.split("_"))-1].split(".")[0]
    nameRoute = serialRead+"_"+timeFormat+"_serial"+str(random.randint(0, 101))+".txt"
    return nameRoute