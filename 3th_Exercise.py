#Código para generar una matriz NxM, con secuencia creciente en zig-zag horizontal

N = input('Ingrese el número de fila: ')
M = input('Ingrese el número de columna: ')

def A(x, y):
    matrix = []
    n = 0; m = -1
    for _ in range(x):
        row = []
        m += 1
        if m % 2 == 1:
            for _ in range (y):
                n += 1
                row.insert(0, n)
            matrix.append(row)
        else:
            for _ in range (y):
                n += 1
                row.append(n)
            matrix.append(row)
    return matrix

if not N.isnumeric() or not M.isnumeric():
    if N.isnumeric():
        raise TypeError('El valor ingresado para columnas debe ser numérico.')
    elif M.isnumeric():
        raise TypeError('El valor ingresado para filas debe ser numérico.')
    else:
        TypeError('Los datos ingresados deben ser numéricos')
    
N = int(N); M = int(M)

if N < 1 or M < 1:
    raise ValueError('Los números ingresados deben ser mayor a cero.')

t = A(N, M)
print(t)
