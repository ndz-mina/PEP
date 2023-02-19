#Realizar matriz NxN, con N dado por el usuario y con cierto patrón.

N = input('Ingrese el tamaño de la matriz cuadrada, este debe ser par y mayor a cero: ')

def A(N:int):

    Matrix = []
    n = 0

    for i in range(N):

        row = []

        for _ in range(N):

            n += 1
            row.append(n)
            
        if i > 1:

            x = i // 2

            if i % 2 == 0:
                Matrix.insert(x, row)
                
            else:
                x += 1
                Matrix.insert(x, row)

        else:                
          Matrix.append(row)

    return Matrix

if not N.isnumeric():
    raise TypeError('El tamaño de la matriz debe ser un número entero.')

N = int(N)

if N == 0 or N % 2 != 0:
    raise ValueError('El valor ingresado debe ser par y mayor que cero.')

Matrix = A(N)
print('La matriz generada será:\n{}'.format(Matrix))
