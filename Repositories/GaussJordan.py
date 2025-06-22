# Implementación del método de Gauss-Jordan
import numpy as np
class GaussJordan:
    def __init__(self, __A=None, __B=None):
        self.__A = __A
        self.__B = __B
        if __A is None or __B is None:
            raise ValueError("Error: Sistema de ecuaciones o resultados nulos")
        
    # Getters
    def getA(self):
        return self.__A
    def getB(self):
        return self.__B
    
    # Setters
    def setA(self, __A=None):
        if __A is None:
            raise ValueError("Error: Matriz A nula")
        self.__A = __A
    def setB(self, __B=None):
        if __B is None:
            raise ValueError("Error: Vector B nulo")
        self.__B = __B
    
    def pivoteafila(self, A,B,vertabla=False):
        A = np.array(A,dtype=float)
        B = np.array(B,dtype=float)
        nB = len(np.shape(B))
        if nB == 1:
            B = np.transpose([B])
        AB  = np.concatenate((A,B),axis=1)
        if vertabla==True:
            print('Matriz aumentada')
            print(AB)
            print('Pivoteo parcial:')
        tamano = np.shape(AB)
        n = tamano[0]
        m = tamano[1]
        pivoteado = 0
        for i in range(0,n-1,1):
            columna = np.abs(AB[i:,i])
            dondemax = np.argmax(columna)
            if (dondemax != 0):
                temporal = np.copy(AB[i,:])
                AB[i,:] = AB[dondemax+i,:]
                AB[dondemax+i,:] = temporal
                pivoteado = pivoteado + 1
                if vertabla==True:
                    print(' ',pivoteado, 'intercambiar filas: ',i,'y', dondemax+i)
        if vertabla==True:
            if pivoteado==0:
                print('  Pivoteo por filas NO requerido')
            else:
                print(AB)
        return(AB)
    
    def gauss_eliminaAdelante(self, AB,vertabla=False,
                              lu=False,casicero = 1e-15):
        tamano = np.shape(AB)
        n = tamano[0]
        m = tamano[1]
        if vertabla==True:
            print('Elimina hacia adelante:')
        for i in range(0,n,1):
            pivote = AB[i,i]
            adelante = i+1
            if vertabla==True:
                print(' fila i:',i,' pivote:', pivote)
            for k in range(adelante,n,1):
                if (np.abs(pivote)>=casicero):
                    factor = AB[k,i]/pivote
                    AB[k,:] = AB[k,:] - factor*AB[i,:]
                    if vertabla==True:
                        print('  fila k:',k,
                            ' factor:',factor)
                else:
                    print('  pivote:', pivote,'en fila:',i,
                        'genera division para cero')
            if vertabla==True:
                print(AB)
        respuesta = np.copy(AB)
        if lu==True: 
            U = AB[:,:n-1]
            respuesta = [AB,L,U]
        return(respuesta)
    
    def gauss_eliminaAtras(self, AB, vertabla=False,
                           precision=5,casicero = 1e-14):
        tamano = np.shape(AB)
        n = tamano[0]
        m = tamano[1]
        ultfila = n-1
        ultcolumna = m-1
        if vertabla==True:
            print('Elimina hacia Atras:')
            np.set_printoptions(precision)
        for i in range(ultfila,0-1,-1):
            pivote = AB[i,i]
            atras = i-1  
            if vertabla==True:
                print(' fila i:',i,' pivote:', pivote)
            for k in range(atras,0-1,-1):
                if np.abs(AB[k,i])>=casicero:
                    factor = AB[k,i]/pivote
                    AB[k,:] = AB[k,:] - factor*AB[i,:]
                    for j in range(0,m,1): 
                        if np.abs(AB[k,j])<=casicero:
                            AB[k,j]=0
                    if vertabla==True:
                        print('  fila k:',k,
                            ' factor:',factor)
                else:
                    print('  pivote:', pivote,'en fila:',i,
                        'genera division para cero')
            AB[i,:] = AB[i,:]/AB[i,i] 
            
            if vertabla==True:
                print(AB)
        X = np.copy(AB[:,ultcolumna])
        return(X)
    
    
# Gauss-Jordan como funciones
# Para implementarlo en el proyecto lo debo adaptar a objetos
# Parametros que usa el constructor
# Métodos de la clase:
# 1. pivoteafila(A, B, vertabla=False)
#          @param: A (sistema de ecuaciones), B (vector con resultados)
#                  Con estos se hace la matriz aumentada AB
# 2. gauss_eliminaAdelante(AB, vertabla=False)
#          @param: AB (matriz aumentada)
# 3. gauss_eliminaAtras(AB, vertabla=False)
#          @param: AB (matriz aumentada)
# En cada una de las funciones. vertabla: se usa para imprimir el procedimiento, true muestra, false no


"""
# Entrada de datos, debe de ir en el Main
A = [[4,-1,1],
     [2,2,-1],
     [6,-2,3]]
B = [4,2,12]
AB = pivoteafila(A,B,vertabla=True)
AB = gauss_eliminaAdelante(AB,vertabla=True)
X = gauss_eliminaAtras(AB,vertabla=True)
# Impresion de resultados
print('solución X: ')
print(X)
"""
