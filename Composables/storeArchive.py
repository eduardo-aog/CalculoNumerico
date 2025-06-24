import random
import time 
from Repositories.Logger import Logger

def storeDataNumbers(archive, arFinal, errorPerArchive, archivesNames):
    if archive == None or arFinal.any == None or errorPerArchive.any == None or archivesNames.any == None:
        Logger.storeArchiveLog("Object-Error: Un objeto es nulo")
        exit()
    
    for m in range(len(arFinal)):
        nameRoute = __storeArchiveFormat(archivesNames[m])
        for i in range(len(arFinal[m])-errorPerArchive[m]):
            if str(arFinal[m][i]) != "nan":
                archive.setOrCreateFiles(nameRoute, arFinal[m][i], i<len(arFinal[m])-1-errorPerArchive[m])
            else:
                continue

def storeDataEcuations(archive, arEcuation, archivesNames):
    if archive == None or arEcuation.any == None or archivesNames == None:
        Logger.storeArchiveLog("Object-Error: Un objeto es nulo")
        exit()
    
    for i in range(len(arEcuation)):
        nameRoute = __storeArchiveFormat(archivesNames[0])
        if str(arEcuation[i]) != "nan":
            archive.setOrCreateFiles(nameRoute, arEcuation[i], i<len(arEcuation[i])-1)
        else:
            continue

def __storeArchiveFormat(nameArchive):
    timeFormat = time.strftime("%Y-%m-%d--%H-%M-%S", time.localtime())
    serialRead = nameArchive.split("_")[len(nameArchive.split("_"))-1].split(".")[0]
    nameRoute = serialRead+"_"+timeFormat+"_serial"+str(random.randint(0, 101))+".txt"
    return nameRoute