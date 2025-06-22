from Repositories.GaussJordan import GaussJordan
import numpy as np

A = np.array([[4,-1,1], [2,2,-1], [6,-2,3]])
B = np.array([4,2,12])
GaussObject = GaussJordan(0, 0)
GaussObject.setA(A)
GaussObject.setB(B)

print("Matriz A: ",GaussObject.getA())
print("Matriz B: ",GaussObject.getB())

AB = GaussObject.pivoteafila(GaussObject.getA(), GaussObject.getB(), vertabla=True)
AB = GaussObject.gauss_eliminaAdelante(AB, vertabla=True)
X = GaussObject.gauss_eliminaAtras(AB, vertabla=True)
print("Solucion X: ")
print(X)
