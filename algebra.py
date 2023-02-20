import modulo_Mina
import numpy as np

def matrix_multiplication(A, B):

    if modulo_Mina.test_matrix(A) == 'Valid' and modulo_Mina.test_matrix(B) == 'Valid':

        order_a = modulo_Mina.len_matrix(A)
        m1 = order_a[0]; n1 = order_a[1]
        order_b = modulo_Mina.len_matrix(B)
        m2 = order_b[0]; n2 = order_b[1]
        C = []

        if n1 == m2:
            A = eval(A)
            B = eval(B)

            for j in range(m1):
                row = []

                for k in range(n2):
                    c = 0

                    for i in range(n1):
                        c += A[j][i] * B[i][k]

                    row.append(c)

                C.append(row)

            x = C

        else:
            x = ValueError
    
    else:
        x = TypeError

    return x

def inverse_gauss_jordan(A):

    if modulo_Mina.test_matrix(A) == 'Valid':
        
        len_matrix = modulo_Mina.len_matrix(A)
        m = len_matrix[0]; n = len_matrix[1]
        deter = determinant(A)

        if m == n and deter != 0:

            A = eval(A); I = modulo_Mina.identy_matrix(m); B = I

            for j in range(m): #Convert A to triangular matrix

                if A[j][j] == 0:

                    cA_0 = A[j]; cB_0 = B[j]; u = 0

                    while A[j+u][j] == 0:

                        u += 1

                        if A[j+u][j] != 0:

                            cA_1 = A[j+u]; cB_1 = B[j+u]

                    A[j] = cA_1; A[j+u] = cA_0
                    B[j] = cB_1; B[j+u] = cB_0
                    d = 1 / A[j][j]

                    for i in range(m):

                        A[j][i] *= d
                        B[j][i] *= d

                    row_op_A = A[j]; row_op_B = B[j]
                    o = j + 1

                    for k in range(o, m):
                        
                        for t in range(m):
                        
                            A[k][t] = A[k][t] - (A[k][j] * row_op_A[t])
                            B[k][t] = B[k][t] - (B[k][j] * row_op_B[t])

                else:
                    d = 1 / A[j][j]

                    for i in range(m):
                    
                        A[j][i] *= d
                        B[j][i] *= d
                    
                    row_op_A = A[j]; row_op_B = B[j]
                    o = j + 1
                    
                    for k in range(o, m):
                    
                        for t in range(m):
                    
                            A[k][t] = A[k][t] - (A[k][j] * row_op_A[t])
                            B[k][t] = B[k][t] - (B[k][j] * row_op_B[t])

            var = m - 1
            
            while var != 0:   #Convert A to identy matrix
                
                for p in range(var):

                    for q in range(m):

                        A[p][q] = A[p][q] - A[p][var] * A[var][q]
                        B[p][q] = B[p][q] -B[p][var] * B[var][q]

                var -= 1
                
            x = B

        else:

            x = ValueError

    else:
        
        x = TypeError

    return x

def cross_product(A,B):

    if modulo_Mina.test_matrix(A) == 'Valid' and modulo_Mina.test_matrix(B) == 'Valid':

        order_a = modulo_Mina.len_matrix(A)
        m1 = order_a[0]; n1 = order_a[1]
        order_b = modulo_Mina.len_matrix(B)

        if m1 == 1 and n1 <= 3 and order_a == order_b:
            A = eval(A)
            B = eval(B)

            if n1 == 2:

                x = 0; y = 0; z = (A[0][0] * B[0][1]) - (A[0][1] * B[0][0])

            else:

                x = (A[0][1] * B[0][2]) - (A[0][2] * B[0][1])
                y = (A[0][2] * B[0][0]) - (A[0][0] * B[0][2])
                z = (A[0][0] * B[0][1]) - (A[0][1] * B[0][0])

            c = print('x = {:.2f}i + {:.2f}j + {:.2f}k\n\
                      x = ({:.2f}, {:.2f}, {:.2f})'.format(x, y, z, x, y, z))

        else:
            c = ValueError
    
    else:
        c = TypeError

    return c

def transpose(A):

    if modulo_Mina.test_matrix(A) == 'Valid':

        order_a = modulo_Mina.len_matrix(A)
        m1 = order_a[0]; n1 = order_a[1]
        C = []

        for _ in range(n1):
            row = []
            for _ in range(m1):
                c = 0
                row.append(c)
            C.append(row)

        A = eval(A)

        for i in range(n1):
            for j in range(m1):
                C[i][j] = A[j][i]

        x = C

    else:
        x = TypeError

    return x

def SLE(*args):

    #Crear función que me entrege una matriz A con los valores de las ecuaciones

    if modulo_Mina.test_matrix(A) == 'Valid':
        
        len_matrix = modulo_Mina.len_matrix(A)
        m = len_matrix[0]; n = len_matrix[1]
        deter = determinant(A)

        if deter != 0:

            A = eval(A); b = eval(b)
            inverse_A = inverse_gauss_jordan(A)
            sol = matrix_multiplication(inverse_A, b)

            x = 'Colocar la sol'

        else:

            if n > m:
               
               x = 'El sistema tiene infinitas soluciones.'

            else:

                x = 'EL sisteme no tiene solución.'

    else:
        
        x = TypeError

    return x

def determinant(A):
    
    if modulo_Mina.test_matrix(A) == 'Valid':
        
        len_matrix = modulo_Mina.len_matrix(A)
        m = len_matrix[0]; n = len_matrix[1]

        if m == n:
            
            A = eval(A)
            A = np.array(A)
            x = np.linalg.det(A)

        else:

            x = ValueError

    else:
        
        x = TypeError

    return x