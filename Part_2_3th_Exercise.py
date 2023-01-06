#Realizar matriz NxN, con N dado por el usuario y con cierto patrón.
N = input('Ingrese el tamaño de la matriz cuadrada: ')
def A(N):
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
if N.isnumeric():
    N = int(N)
    Matrix = A(N)
    print('La matriz generada será:\n{}'.format(Matrix))
else:
    print('Error en el dato ingresado.')