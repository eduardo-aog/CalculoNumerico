# Implementacion del metodo Gauss-Seidel
import numpy as np
class GaussSeidel:
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
    
    def gaussSeidel(A=None,B=None,X0=None,tolera=0, iteramax=100, vertabla=False, precision=4):
        A = np.array(A, dtype=float)
        B = np.array(B, dtype=float)
        X0 = np.array(X0, dtype=float)
        tamano = np.shape(A)
        n = tamano[0]
        m = tamano[1]
        diferencia = 2*tolera*np.ones(n, dtype=float)
        errado = 2*tolera 
        tabla = [np.copy(X0)]
        tabla = np.concatenate((tabla,[[np.nan]]),axis=1)
        if vertabla==True:
            np.set_printoptions(precision)
        itera = 0
        X = np.copy(X0)
        while (errado>tolera and itera<iteramax):
            for i in range(0,n,1):
                suma = B[i]
                for j in range(0,m,1):
                    if (i!=j):
                        suma = suma-A[i,j]*X[j]
                nuevo = suma/A[i,i]
                diferencia[i] = np.abs(nuevo-X[i])
                X[i] = nuevo
            errado = np.max(diferencia)
            Xfila= np.concatenate((X,[errado]),axis=0)
            tabla = np.concatenate((tabla,[Xfila]),axis = 0)
            itera = itera + 1
        if (itera>iteramax):
            X = np.nan
            print('No converge,iteramax superado')
        return(X,tabla)

    def pivoteaFila(A,B):
        A = np.array(A,dtype=float)
        B = np.array(B,dtype=float)
        nB = len(np.shape(B))
        if nB == 1:
            B = np.transpose([B])
        AB  = np.concatenate((A,B),axis=1)
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
        return(AB)