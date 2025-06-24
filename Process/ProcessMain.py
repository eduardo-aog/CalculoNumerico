from .Process import checkEcuations
from Composables.storeArchive import storeDataEcuations

#[0] las ecuaciones [1]el nombre del archivo que se consiguio
def processMain(archive, ecuationMatrix, arFinal): 
    arrayResults = checkEcuations(arFinal, ecuationMatrix[0])
    storeDataEcuations(archive, arrayResults, ecuationMatrix[1])