from .Process import aproxValue
from .Process import exactValue
from Repositories.ErrorObj import Error
from Repositories.AbsError import AbsoluteError
from Repositories.RelError import RelativeError

def ProcessMain(values): 
    measuredValue = aproxValue(values)
    realValue = exactValue(values)
    errorObj = Error(0.0, 0.0)
    errorObj.setMeasuredValue(measuredValue)
    errorObj.setRealValue(realValue)    
    
    absErrorObject = AbsoluteError(errorObj.getMeasuredValue(), errorObj.getRealValue())
    absErrorCalc = absErrorObject.calcErrorAbs()
    
    relativeErrorObject = RelativeError(errorObj.getMeasuredValue(), errorObj.getRealValue())
    relativeErrorCalc = relativeErrorObject.calcErrorRel()
    
    return measuredValue, realValue, absErrorCalc, relativeErrorCalc