#Cálculo aproximado del valor pi según una cantidad dada, por el usuario, de términos.
M = input('Ingrese la cantidad de términos a sumar : ')
def series(k):
    suma = 0
    for n in range(1, k + 1):
        suma = suma + (((-1)**(n - 1))/(n**6))
    return suma
def word(x):
    if x == 1:
        c = 'valor'
    else:
        c = 'valores'
    return c
if M.isnumeric():
    M = int(M)
    Aprox_pi = (30240 * series(M) / 31)**(1 / 6)
    print('El valor de la aproximación de pi con {} {} es {}'.format(M, word(M), Aprox_pi))
else:
    print('Error en el valor ingresado.')