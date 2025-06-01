def showCase(measuredValue, realValue, absoluteError, relativeError, roundError, truncError, propError):
    print("Valor medido: ",measuredValue)
    print("Valor real: ", realValue)
    print("Error absoluto de la medida: ",absoluteError)
    print("Error relativo de la medida: ",relativeError)
    print("Error relativo de la medida en porcentaje: ",relativeError*100,"% ")
    print("Error por redondeo: ",roundError)
    print("Error por truncamiento: ",truncError)
    print("Error de propagacion: ",propError)
    
