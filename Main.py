from Process.ProcessMain import ProcessMain
from Helpers.ConsultMain import ConsultMain

def Main():
# Inicializacion
    values = [[20.7,70.3,90.8],[18,30.7,10.1],[60,60.33,10.8],[80,600,30.123]]  
    
# Proceso
    measuredValue, realValue, absoluteError, relativeError = ProcessMain(values)    
    
# Impresion de resultados
    ConsultMain(measuredValue, realValue, absoluteError, relativeError)
    print("Fin del programa")
    
# Eliminacion de instancias
    values = None
    realValue = 0.0
    measuredValue = 0.0
    absoluteError = 0.0
    relativeError = 0.0

# Llamada a la funcion 
Main()