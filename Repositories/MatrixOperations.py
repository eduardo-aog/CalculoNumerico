import numpy as np

class MatrixOperations:
    def __utilMatrixSum(self, matrix1: np.ndarray, matrix2: np.ndarray):
        """Suma dos matrices"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        if rows1 != rows2 or cols1 != cols2:
            return False
        result = np.zeros((rows1, cols1))
        for i in range(rows1):
            for j in range(cols1):
                result[i, j] = matrix1[i, j] + matrix2[i, j]
        return result

    def __utilMatrixMinus(self, matrix1: np.ndarray, matrix2: np.ndarray):
        """Resta dos matrices"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        if rows1 != rows2 or cols1 != cols2:
            return False
        result = np.zeros((rows1, cols1))
        for i in range(rows1):
            for j in range(cols1):
                result[i, j] = matrix1[i, j] - matrix2[i, j]
        return result

    def __utilMatrixMult(self, matrix1: np.ndarray, matrix2: np.ndarray):
        """Multiplica dos matrices"""
        rows1 = len(matrix1)
        cols1 = len(matrix1[0])
        rows2 = len(matrix2)
        cols2 = len(matrix2[0])
        if cols1 != rows2:
            return False
        result = np.zeros((rows1, cols2))
        for i in range(rows1):
            for j in range(cols2):
                sum_val = 0
                for k in range(cols1):
                    sum_val += matrix1[i, k] * matrix2[k, j]
                result[i, j] = sum_val
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
        temp = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                temp[i, j] = matrix[i, j]
        det = 1
        for i in range(n):
            max_row = i
            for k in range(i+1, n):
                if abs(temp[k, i]) > abs(temp[max_row, i]):
                    max_row = k
            if temp[max_row, i] == 0:
                return 0
            if max_row != i:
                for j in range(n):
                    temp[i, j], temp[max_row, j] = temp[max_row, j], temp[i, j]
                det *= -1
            det *= temp[i, i]
            for k in range(i+1, n):
                factor = temp[k, i] / temp[i, i]
                for j in range(i, n):
                    temp[k, j] -= factor * temp[i, j]
        return det

    def __utilMatrixInverse(self, matrix: np.ndarray):
        """Calcula la inversa de una matriz cuadrada"""
        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return False
        aug = np.zeros((n, 2*n))
        for i in range(n):
            for j in range(n):
                aug[i, j] = matrix[i, j]
            for j in range(n):
                aug[i, n+j] = 1 if i == j else 0
        for i in range(n):
            max_row = i
            for k in range(i+1, n):
                if abs(aug[k, i]) > abs(aug[max_row, i]):
                    max_row = k
            if aug[max_row, i] == 0:
                return False
            if max_row != i:
                for j in range(2*n):
                    aug[i, j], aug[max_row, j] = aug[max_row, j], aug[i, j]
            pivot = aug[i, i]
            for j in range(2*n):
                aug[i, j] /= pivot
            for k in range(n):
                if k != i:
                    factor = aug[k, i]
                    for j in range(2*n):
                        aug[k, j] -= factor * aug[i, j]
        inv = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                inv[i, j] = aug[i, n+j]
        return inv

    def __utilMatrixRank(self, matrix: np.ndarray):
        """Calcula el rango de una matriz"""
        m = len(matrix)
        n = len(matrix[0])
        temp = np.zeros((m, n))
        for i in range(m):
            for j in range(n):
                temp[i, j] = matrix[i, j]
        rank = 0
        row_selected = [False] * m
        for i in range(n):
            j = 0
            while j < m:
                if not row_selected[j] and abs(temp[j, i]) > 1e-10:
                    break
                j += 1
            if j < m:
                rank += 1
                row_selected[j] = True
                for p in range(n):
                    if p != i:
                        factor = temp[j, p] / temp[j, i]
                        for k in range(m):
                            temp[k, p] -= factor * temp[k, i]
        return rank

    def __utilMatrixEigenvalues(self, matrix: np.ndarray, max_iter=100, tol=1e-10):
        """Calcula los valores propios de una matriz cuadrada (método de potencias)"""
        n = len(matrix)
        for row in matrix:
            if len(row) != n:
                return False
        b_k = np.ones((n, 1))
        for _ in range(max_iter):
            b_k1 = np.zeros((n, 1))
            for i in range(n):
                for j in range(n):
                    b_k1[i, 0] += matrix[i, j] * b_k[j, 0]
            norm = 0
            for i in range(n):
                norm += b_k1[i, 0] ** 2
            norm = norm ** 0.5
            if norm == 0:
                return 0
            for i in range(n):
                b_k1[i, 0] /= norm
            close = True
            for i in range(n):
                if abs(b_k[i, 0] - b_k1[i, 0]) > tol:
                    close = False
                    break
            if close:
                break
            b_k = b_k1
        num = 0
        den = 0
        for i in range(n):
            for j in range(n):
                num += b_k[i, 0] * matrix[i, j] * b_k[j, 0]
            den += b_k[i, 0] ** 2
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