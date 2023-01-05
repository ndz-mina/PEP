#Código para generar una matriz NxM, con secuencia creciente en zig-zag horizontal
def A(x, y):
    matrix = []
    n = 0; m = -1
    for i in range(x):
        row = []
        m += 1
        if m % 2 == 1:
            for j in range (y):
                n += 1
                row.insert(0, n)
            matrix.append(row)
        else:
            for j in range (y):
                n += 1
                row.append(n)
            matrix.append(row)
    return matrix

N = input('Ingrese el número de fila: ')
if N.isnumeric():
    M = input('Ingrese el número de columna: ')
    if M.isnumeric():
        N = int(N); M = int(M)
        t = A(N, M)
        print(t)
    else:
        print('Error en el número de columnas.')
else:
    print('Error en el número de filas.')