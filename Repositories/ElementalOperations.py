class ElementalOperations:
    __num = ""
    __op = ""

    def __init__(self, num):
        self.__utilValNum(num)
        self.__utilValOp(self.__num)

    def __utilValNum(self, num):
        if num == None:
            raise ValueError("Valor nulo no permitido")
        if not self.__utilValNegativeFormat(num):
            raise ValueError("Valor negativo con formato no permitido")
        if "," in num:
            num = self.__utilReplaceCommaFraction(num)
        if not self.__utilValFractionFormat(num):
            raise ValueError("Valor de fracción con formato no permitido")
        if not self.__utilValSpecialChar(num):
            raise ValueError("Valor no permitido, no es un número")
        self.__num = num

    def __utilValOp(self, num):
        op = ""
        op = self.__utilOpHex(num, op)
        op = self.__utilOpDec(num, op)
        op = self.__utilOpBin(num, op)
        if op == "":
            raise ValueError("Valor no permitido, no es un número")
        self.__op = op

    def __utilOpBin(self, num, op):
        for i in num:
            if i not in "01":
                return op
        sum = self.__utilBinSum(num, num)
        minus = self.__utilBinMinus(num, num)
        product = self.__utilBinMult(num, "10")
        div = self.__utilBinDiv(num, "10")
        
        return "+, -, *, /, +(Concatenacion)"

    def __utilOpDec(self, num, op):
        for i in num:
            if i not in "-,.0123456789":
                return op
        if not self.__utilDecSum(num, num):
            return ""   
        if not self.__utilDecMinus(num, num):
            return ""
        if not self.__utilDecMult(num, "2"):
            return ""
        if not self.__utilDecDiv(num, "2"):
            return ""
        
        return "+, -, *, /, +(Concatenacion)"

    def __utilOpHex(self, num, op):
        for i in num:
            if i.lower() not in "0123456789abcdef":
                return op
        conc = num+num

        return "+(Concatenacion)"
    
    def __utilTrueOneButNotBoth(self, a, b):
        if (a or b) and not(a and b):
            return True
        return False
    
    def __utilLargerNumber(self, num1, num2):
        if len(num2) < len(num1):
            for i in range(len(num1)-len(num2)):
                num2 = "0" + num2
        return num2
    
    def __utilBinSum(self, num1, num2):
        sum = ""
        carry = "0"

        num2 = self.__utilLargerNumber(num1, num2)
        num1 = self.__utilLargerNumber(num2, num1)       
        for i in range(len(num1)):
            lastToFirst = len(num1)-1-i
            bin1 = num1[lastToFirst]=="1"
            bin2 = num2[lastToFirst]=="1"
            if self.__utilTrueOneButNotBoth(bin1, bin2) and carry=="0":
                sum = "1" + sum
            elif not self.__utilTrueOneButNotBoth(bin1, bin2) and carry=="1":
                sum = "1" + sum
            else:
                sum = "0" + sum
            if bin1 and bin2:
                carry = "1"
            elif self.__utilTrueOneButNotBoth(bin1, bin2) and carry =="1":
                carry = "1"
            else:
                carry = "0"               
        if carry=="1":
            sum = "1" + sum 

        return sum, carry
    
    def __utilComplement1(self, num):
        inverseValue = ""
        for i in range(len(num)):
            lastToFirst = len(num)-1-i
            if num[lastToFirst]=="1":
                inverseValue = "0" + inverseValue
            elif num[lastToFirst]=="0":
                inverseValue = "1" + inverseValue
        return inverseValue
                
    def __utilBinMinus(self, num1, num2):
        inverseValue = ""
        minus = ""
        carry = "0"

        num2 = self.__utilLargerNumber(num1, num2)
        num1 = self.__utilLargerNumber(num2, num1) 
        inverseValue = self.__utilComplement1(num2)
        minus, carry = self.__utilBinSum(num1, inverseValue)
        if carry=="1":
            minus = self.__utilBinSum(minus, carry)
        else:
            inverseValue = self.__utilComplement1(minus)
            minus = "-" + inverseValue
        
        return minus
    
    def __utilBinMult(self, num1, num2):
        product = ""
        mult = num1

        for i in range(len(num2)):
            lastToFirst = len(num2)-1-i
            if num2[lastToFirst]=="1" and i!=0:
                product = self.__utilBinSum(num1, mult)[0] + product
                mult = mult + "0"
            else:
                mult = mult + "0"
        
        return product

    def __utilBinDiv(self, num1, num2):
        digsForOperation = ""
        result = ""
        carry = ""

        if num2!="0":
            for i in range(len(num1)):
                if len(digsForOperation)<len(num2):
                    digsForOperation = digsForOperation + num1[i]
                    if result!="":
                        result = result + "0"
                else:
                    carry = self.__utilBinMinus(digsForOperation, num2)
                if carry=="1" or digsForOperation==num2:
                    result = result + "1"
                    if digsForOperation==num2:
                        carry = ""
                elif carry=="0":
                    result = result + "0"
                    carry = ""
                digsForOperation = carry

        return result   
                
    #Pueden arrojar ValueError las op decimales
    def __utilDecSum(self, num1, num2): 
        test = str(float(num1) + float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecMinus(self, num1, num2):
        test = str(float(num1) - float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecMult(self, num1, num2):
        test = str(float(num1) * float(num2)) 
        for i in test:
            if i not in "-,.0123456789":
                return False
        return True
    
    def __utilDecDiv(self, num1, num2):
        if float(num2)!=0:
            test = str(float(num1) / float(num2)) 
            for i in test:
                if i not in "-,.0123456789":
                    return False               
        return True

    def __utilValNegativeFormat(self, num):
        n = 0
        for i in num:
            if "-" in num and (n == 0 and i!= "-"):
                return False
            if i == "-":
                return True
            n += 1
        return True

    def __utilValFractionFormat(self, num):
        n = 0
        for i in num:
            if "." in num and (n == 0 and i == "."):
                return False
            if ("." in num and "-" in num) and (n == 1 and i == "."):
                return False
            if i == ".":
                return True
            n += 1
        return True   
    
    def __utilValSpecialChar(self, num):
        specialChars = "qwrtyuiopsghjklñzxvnm|°¬!#$%&/()=?¡'¿´+{}[];:_¨* "
        for i in num:
            if i.lower() in specialChars:
                return False
        return True
    
    def __utilReplaceCommaFraction(self, digit):
        commaless = digit.split(",")
        return commaless[0]+"."+commaless[1]

    def getNum(self):
        return self.__num

    def getOperation(self):
        return self.__op

    def __utilValMatrixFormat(self, matrix_str):
        """Valida el formato de una matriz representada como string"""
        if matrix_str == None:
            return False
        
        if len(matrix_str) < 2 or matrix_str[0] != '[' or matrix_str[-1] != ']':
            return False
        
        content = matrix_str[1:-1]
        if len(content) == 0:
            return False
        
        rows = self.__utilSplitMatrixRows(content)
        if len(rows) == 0:
            return False
        
        first_row_length = len(self.__utilSplitRowElements(rows[0]))
        for row in rows:
            elements = self.__utilSplitRowElements(row)
            if len(elements) != first_row_length:
                return False
            for element in elements:
                if not self.__utilValNum(element.strip()):
                    return False
        
        return True

    def __utilSplitMatrixRows(self, content):
        """Divide el contenido de una matriz en filas"""
        rows = []
        current_row = ""
        bracket_count = 0
        
        for char in content:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
            
            current_row += char
            
            if bracket_count == 0 and char == ']':
                rows.append(current_row)
                current_row = ""
        
        return rows

    def __utilSplitRowElements(self, row):
        """Divide una fila en elementos individuales"""
        elements = []
        current_element = ""
        bracket_count = 0
        
        for char in row:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
            elif char == ',' and bracket_count == 1:
                elements.append(current_element)
                current_element = ""
                continue
            
            current_element += char
        
        if current_element:
            elements.append(current_element)
        
        return elements

    def __utilMatrixToArray(self, matrix_str):
        """Convierte una matriz en string a array bidimensional"""
        if not self.__utilValMatrixFormat(matrix_str):
            return None
        
        content = matrix_str[1:-1]
        rows = self.__utilSplitMatrixRows(content)
        matrix = []
        
        for row in rows:
            elements = self.__utilSplitRowElements(row)
            row_array = []
            for element in elements:
                row_array.append(float(element.strip()))
            matrix.append(row_array)
        
        return matrix

    def __utilArrayToMatrix(self, matrix_array):
        """Convierte un array bidimensional a string de matriz"""
        if not matrix_array or len(matrix_array) == 0:
            return "[]"
        
        matrix_str = "["
        for i, row in enumerate(matrix_array):
            matrix_str += "["
            for j, element in enumerate(row):
                matrix_str += str(element)
                if j < len(row) - 1:
                    matrix_str += ", "
            matrix_str += "]"
            if i < len(matrix_array) - 1:
                matrix_str += ", "
        matrix_str += "]"
        
        return matrix_str

    def __utilMatrixSum(self, matrix1_str, matrix2_str):
        """Suma dos matrices"""
        matrix1 = self.__utilMatrixToArray(matrix1_str)
        matrix2 = self.__utilMatrixToArray(matrix2_str)
        
        if matrix1 is None or matrix2 is None:
            return False
        
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return False
        
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] + matrix2[i][j])
            result.append(row)
        
        return self.__utilArrayToMatrix(result)

    def __utilMatrixMinus(self, matrix1_str, matrix2_str):
        """Resta dos matrices"""
        matrix1 = self.__utilMatrixToArray(matrix1_str)
        matrix2 = self.__utilMatrixToArray(matrix2_str)
        
        if matrix1 is None or matrix2 is None:
            return False
        
        if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
            return False
        
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix1[0])):
                row.append(matrix1[i][j] - matrix2[i][j])
            result.append(row)
        
        return self.__utilArrayToMatrix(result)

    def __utilMatrixMult(self, matrix1_str, matrix2_str):
        """Multiplica dos matrices"""
        matrix1 = self.__utilMatrixToArray(matrix1_str)
        matrix2 = self.__utilMatrixToArray(matrix2_str)
        
        if matrix1 is None or matrix2 is None:
            return False
        
        if len(matrix1[0]) != len(matrix2):
            return False
        
        result = []
        for i in range(len(matrix1)):
            row = []
            for j in range(len(matrix2[0])):
                sum_val = 0
                for k in range(len(matrix1[0])):
                    sum_val += matrix1[i][k] * matrix2[k][j]
                row.append(sum_val)
            result.append(row)
        
        return self.__utilArrayToMatrix(result)

    def __utilMatrixScalarMult(self, matrix_str, scalar):
        """Multiplica una matriz por un escalar"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        result = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[0])):
                row.append(matrix[i][j] * scalar)
            result.append(row)
        
        return self.__utilArrayToMatrix(result)

    def __utilMatrixTranspose(self, matrix_str):
        """Calcula la transpuesta de una matriz"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        result = []
        for j in range(len(matrix[0])):
            row = []
            for i in range(len(matrix)):
                row.append(matrix[i][j])
            result.append(row)
        
        return self.__utilArrayToMatrix(result)

    def __utilMatrixDeterminant(self, matrix_str):
        """Calcula el determinante de una matriz cuadrada"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        if len(matrix) != len(matrix[0]):
            return False
        
        return self.__utilCalculateDeterminant(matrix)

    def __utilCalculateDeterminant(self, matrix):
        """Calcula el determinante usando eliminación gaussiana"""
        n = len(matrix)
        
        if n == 1:
            return matrix[0][0]
        
        if n == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        temp_matrix = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[i][j])
            temp_matrix.append(row)
        
        det = 1
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(temp_matrix[k][i]) > abs(temp_matrix[max_row][i]):
                    max_row = k
            
            if max_row != i:
                temp_matrix[i], temp_matrix[max_row] = temp_matrix[max_row], temp_matrix[i]
                det = -det
            
            if temp_matrix[i][i] == 0:
                return 0
            
            for k in range(i + 1, n):
                factor = temp_matrix[k][i] / temp_matrix[i][i]
                for j in range(i, n):
                    temp_matrix[k][j] -= factor * temp_matrix[i][j]
        
        for i in range(n):
            det *= temp_matrix[i][i]
        
        return det

    def __utilMatrixInverse(self, matrix_str):
        """Calcula la inversa de una matriz cuadrada"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        if len(matrix) != len(matrix[0]):
            return False
        
        det = self.__utilCalculateDeterminant(matrix)
        if det == 0:
            return False
        
        n = len(matrix)
        
        augmented = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(matrix[i][j])
            for j in range(n):
                row.append(1 if i == j else 0)
            augmented.append(row)
        
        for i in range(n):
            max_row = i
            for k in range(i + 1, n):
                if abs(augmented[k][i]) > abs(augmented[max_row][i]):
                    max_row = k
            
            if max_row != i:
                augmented[i], augmented[max_row] = augmented[max_row], augmented[i]
            
            if augmented[i][i] == 0:
                return False
            
            pivot = augmented[i][i]
            for j in range(2 * n):
                augmented[i][j] /= pivot
            
            for k in range(n):
                if k != i:
                    factor = augmented[k][i]
                    for j in range(2 * n):
                        augmented[k][j] -= factor * augmented[i][j]
        
        inverse = []
        for i in range(n):
            row = []
            for j in range(n, 2 * n):
                row.append(augmented[i][j])
            inverse.append(row)
        
        return self.__utilArrayToMatrix(inverse)

    def __utilMatrixRank(self, matrix_str):
        """Calcula el rango de una matriz"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        m, n = len(matrix), len(matrix[0])
        
        temp_matrix = []
        for i in range(m):
            row = []
            for j in range(n):
                row.append(matrix[i][j])
            temp_matrix.append(row)
        
        rank = 0
        for col in range(n):
            pivot_row = -1
            for row in range(rank, m):
                if temp_matrix[row][col] != 0:
                    pivot_row = row
                    break
            
            if pivot_row != -1:
                if pivot_row != rank:
                    temp_matrix[rank], temp_matrix[pivot_row] = temp_matrix[pivot_row], temp_matrix[rank]
                
                pivot = temp_matrix[rank][col]
                for j in range(n):
                    temp_matrix[rank][j] /= pivot
                
                for i in range(rank + 1, m):
                    factor = temp_matrix[i][col]
                    for j in range(n):
                        temp_matrix[i][j] -= factor * temp_matrix[rank][j]
                
                rank += 1
        
        return rank

    def __utilMatrixEigenvalues(self, matrix_str):
        """Calcula los valores propios de una matriz cuadrada (método de potencias)"""
        matrix = self.__utilMatrixToArray(matrix_str)
        
        if matrix is None:
            return False
        
        if len(matrix) != len(matrix[0]):
            return False
        
        n = len(matrix)
        
        vector = [1.0] * n
        tolerance = 1e-10
        max_iterations = 100
        
        for iteration in range(max_iterations):
            new_vector = [0.0] * n
            for i in range(n):
                for j in range(n):
                    new_vector[i] += matrix[i][j] * vector[j]
            
            norm = 0.0
            for val in new_vector:
                norm += val * val
            norm = norm ** 0.5
            
            if norm == 0:
                return False
            
            for i in range(n):
                new_vector[i] /= norm
            
            eigenvalue = 0.0
            for i in range(n):
                for j in range(n):
                    eigenvalue += new_vector[i] * matrix[i][j] * new_vector[j]
            
            diff = 0.0
            for i in range(n):
                diff += abs(new_vector[i] - vector[i])
            
            if diff < tolerance:
                return eigenvalue
            
            vector = new_vector
        
        return False

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