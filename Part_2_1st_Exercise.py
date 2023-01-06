#Código para saber el porcentajes de números menores a N, dado por el usuario,
#cuya cadena llega a 89.
N = input('Ingrese un valor numérico: ')
def porcent(x, y):
    num_porcent = x * 100 / y
    return num_porcent
def str_num(x):
    while x != 1 and x != 89:
        sum = 0
        digit = str(x)
        for i in digit:
            y = int(i)
            sum += y ** 2
        x = sum
    if x == 1:
        c = 0
    elif x == 89:
        c = 1
    return c
if N.isnumeric():
    N = int(N); count = 0
    if N > 1:
        for x in range(1, N):
            count += str_num(x)
        pct = porcent(count, N)
        rest = 100 - pct
        print('El porcentaje de números menor a {}, cuyo los números cadenas llegan a 89 es de: {:.2f}%\nMientras los que llegan a 1 es de: {:.2f}%'. format(N, pct, rest))
    elif N <= 1:
        pct = 0
else:
    print('Error en el valor ingresado.')