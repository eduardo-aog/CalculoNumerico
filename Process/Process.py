def aproxValue(values):
    if values != None:
        sum = 0
        for i in values:
            for k in i:
                sum += k
        average = sum / 12
        return average
    else:
        print("Datos nulos. Fin del programa")

def exactValue(values):
    if values != None:
        sum = 0
        ki = 0
        for i in values:
            for k in i:
                ki = k+0.01
                sum += ki
        average = sum / 12
        return average
    else:
        print("Datos nulos. Fin del programa")
