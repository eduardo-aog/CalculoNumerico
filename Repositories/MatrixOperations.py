import numpy as np

class MatrixOperations:
    def __utilMatrixSum(self, matrixOne: np.ndarray, matrixTwo: np.ndarray):
        """Suma dos matrices"""
        rowsOne = len(matrixOne)
        colsOne = len(matrixOne[0])
        rowsTwo = len(matrixTwo)
        colsTwo = len(matrixTwo[0])
        if rowsOne != rowsTwo or colsOne != colsTwo:
            return False
        result = np.zeros((rowsOne, colsOne))
        for i in range(rowsOne):
            for j in range(colsOne):
                result[i, j] = matrixOne[i, j] + matrixTwo[i, j]
        return result

    def __utilMatrixMinus(self, matrixOne: np.ndarray, matrixTwo: np.ndarray):
        """Resta dos matrices"""
        rowsOne = len(matrixOne)
        colsOne = len(matrixOne[0])
        rowsTwo = len(matrixTwo)
        colsTwo = len(matrixTwo[0])
        if rowsOne != rowsTwo or colsOne != colsTwo:
            return False
        result = np.zeros((rowsOne, colsOne))
        for i in range(rowsOne):
            for j in range(colsOne):
                result[i, j] = matrixOne[i, j] - matrixTwo[i, j]
        return result

    def __utilMatrixMult(self, matrixOne: np.ndarray, matrixTwo: np.ndarray):
        """Multiplica dos matrices"""
        rowsOne = len(matrixOne)
        colsOne = len(matrixOne[0])
        rowsTwo = len(matrixTwo)
        colsTwo = len(matrixTwo[0])
        if colsOne != rowsTwo:
            return False
        result = np.zeros((rowsOne, colsTwo))
        for i in range(rowsOne):
            for j in range(colsTwo):
                sumVal = 0
                for k in range(colsOne):
                    sumVal += matrixOne[i, k] * matrixTwo[k, j]
                result[i, j] = sumVal
        return result

    def __utilMatrixScalarMult(self, matrix: np.ndarray, scalar: float):
        """Multiplica una matriz por un escalar"""
        rows = len(matrix)
        cols = len(matrix[0])
        result = np.zeros((rows, cols))
        for i in range(rows):
            for j in range(cols):
                result[i, j] = matrix[i, j] * scalar
        return result

    def __utilMatrixTranspose(self, matrix: np.ndarray):
        """Calcula la transpuesta de una matriz"""
        rows = len(matrix)
        cols = len(matrix[0])
        result = np.zeros((cols, rows))
        for i in range(rows):
            for j in range(cols):
                result[j, i] = matrix[i, j]
        return result

    def __utilMatrixDeterminant(self, matrix: np.ndarray):
        """Calcula el determinante de una matriz cuadrada"""
        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return False
        tempMatrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                tempMatrix[i, j] = matrix[i, j]
        det = 1
        for i in range(n):
            maxRow = i
            for k in range(i+1, n):
                if abs(tempMatrix[k, i]) > abs(tempMatrix[maxRow, i]):
                    maxRow = k
            if tempMatrix[maxRow, i] == 0:
                return 0
            if maxRow != i:
                for j in range(n):
                    tempMatrix[i, j], tempMatrix[maxRow, j] = tempMatrix[maxRow, j], tempMatrix[i, j]
                det *= -1
            det *= tempMatrix[i, i]
            for k in range(i+1, n):
                factor = tempMatrix[k, i] / tempMatrix[i, i]
                for j in range(i, n):
                    tempMatrix[k, j] -= factor * tempMatrix[i, j]
        return det

    def __utilMatrixInverse(self, matrix: np.ndarray):
        """Calcula la inversa de una matriz cuadrada"""
        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return False
        augMatrix = np.zeros((n, 2*n))
        for i in range(n):
            for j in range(n):
                augMatrix[i, j] = matrix[i, j]
            for j in range(n):
                augMatrix[i, n+j] = 1 if i == j else 0
        for i in range(n):
            maxRow = i
            for k in range(i+1, n):
                if abs(augMatrix[k, i]) > abs(augMatrix[maxRow, i]):
                    maxRow = k
            if augMatrix[maxRow, i] == 0:
                return False
            if maxRow != i:
                for j in range(2*n):
                    augMatrix[i, j], augMatrix[maxRow, j] = augMatrix[maxRow, j], augMatrix[i, j]
            pivot = augMatrix[i, i]
            for j in range(2*n):
                augMatrix[i, j] /= pivot
            for k in range(n):
                if k != i:
                    factor = augMatrix[k, i]
                    for j in range(2*n):
                        augMatrix[k, j] -= factor * augMatrix[i, j]
        invMatrix = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                invMatrix[i, j] = augMatrix[i, n+j]
        return invMatrix

    def __utilMatrixRank(self, matrix: np.ndarray):
        """Calcula el rango de una matriz"""
        m = len(matrix)
        n = len(matrix[0])
        tempMatrix = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                tempMatrix[i, j] = matrix[i, j]
        rank = 0
        rowSelected = [False] * m
        for i in range(n):
            j = 0
            while j < m:
                if not rowSelected[j] and abs(tempMatrix[j, i]) > 1e-10:
                    break
                j += 1
            if j < m:
                rank += 1
                rowSelected[j] = True
                for p in range(n):
                    if p != i:
                        factor = tempMatrix[j, p] / tempMatrix[j, i]
                        for k in range(m):
                            tempMatrix[k, p] -= factor * tempMatrix[k, i]
        return rank

    def __utilMatrixEigenvalues(self, matrix: np.ndarray, maxIter=100, tol=1e-10):
        """Calcula los valores propios de una matriz cuadrada (método de potencias)"""
        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return False
        bK = np.ones((n, 1))
        for _ in range(maxIter):
            bK1 = np.zeros((n, 1))
            for i in range(n):
                for j in range(n):
                    bK1[i, 0] += matrix[i, j] * bK[j, 0]
            norm = 0
            for i in range(n):
                norm += bK1[i, 0] ** 2
            norm = norm ** 0.5
            if norm == 0:
                return 0
            for i in range(n):
                bK1[i, 0] /= norm
            close = True
            for i in range(n):
                if abs(bK[i, 0] - bK1[i, 0]) > tol:
                    close = False
                    break
            if close:
                break
            bK = bK1
        num = 0
        den = 0
        for i in range(n):
            for j in range(n):
                num += bK[i, 0] * matrix[i, j] * bK[j, 0]
            den += bK[i, 0] ** 2
        return num / den

    def getMatrixOperations(self, matrix_str):
        """Retorna las operaciones disponibles para una matriz"""
        if not self.__utilValMatrixFormat(matrix_str):
            return ""
        
        matrix = self.__utilMatrixToArray(matrix_str)
        if matrix is None:
            return ""
        
        operations = "+, -, *, T(Transpuesta), det(Determinante), inv(Inversa), rank(Rango), eigen(Valores propios)"
        
        if len(matrix) == len(matrix[0]):
            operations += ", det, inv, eigen"
        
        return operations