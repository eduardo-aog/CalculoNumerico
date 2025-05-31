from .Process import aproxValue
from .Process import exactValue
from Repositories.ErrorObj import Error
from Repositories.AbsError import AbsoluteError
from Repositories.RelError import RelativeError

def ProcessMain(values): 
    measuredValue = aproxValue(values)
    realValue = exactValue(values)
    errorObject = Error(measuredValue, realValue)
    
    absErrorObject = AbsoluteError(errorObject.measuredValue, errorObject.realValue)
    absErrorCalc = absErrorObject.calcErrorAbs()
    
    relativeErrorObject = RelativeError(errorObject.measuredValue, errorObject.realValue)
    relativeErrorCalc = relativeErrorObject.calcErrorRel()
    
    return measuredValue, realValue, absErrorCalc, relativeErrorCalc