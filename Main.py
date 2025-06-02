from Process.ProcessMain import ProcessMain
from Helpers.ConsultMain import ConsultMain

def Main():
# Inicializacion
    measured = 9.5
    real = 10.67
        
# Proceso
    measuredValue, realValue, absoluteError, relativeError, roundError, truncError, propError = ProcessMain(measured, real)    
    
# Impresion de resultados
    ConsultMain(measuredValue, realValue, absoluteError, relativeError, roundError, truncError, propError)
    print("Fin del programa")

# Llamada a la funcion 
Main()
