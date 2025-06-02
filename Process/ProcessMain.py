from Repositories.ErrorObj import Error
from Repositories.AbsError import AbsoluteError
from Repositories.RelError import RelativeError
from Repositories.RoundError import RoundError
from Repositories.TruncError import TruncError
from Repositories.PropError import PropagationError

def ProcessMain(measuredValue, realValue): 
    errorObj = Error(0.0, 0.0)
    errorObj.setMeasuredValue(measuredValue)
    errorObj.setRealValue(realValue)    
    
    absErrorObject = AbsoluteError(errorObj.getMeasuredValue(), errorObj.getRealValue())
    absErrorCalc = absErrorObject.calcErrorAbs()
    
    relativeErrorObject = RelativeError(errorObj.getMeasuredValue(), errorObj.getRealValue())
    relativeErrorCalc = relativeErrorObject.calcErrorRel()
    
    roundErrorObject = RoundError(errorObj.getRealValue())
    roundErrorCalc = roundErrorObject.calcErrorAbs()

    truncErrorObject = TruncError(errorObj.getRealValue())
    truncErrorCalc = truncErrorObject.calcErrorAbs()
    
    propErrorObject = PropagationError(errorObj.getRealValue())
    propErrorCalc = propErrorObject.calcErrorAbs()
    
    return measuredValue, realValue, absErrorCalc, relativeErrorCalc, roundErrorCalc, truncErrorCalc, propErrorCalc
