#Código para generar un número pseudoaleatoreo usando 
#la técnica del cuadrado medio para dígitos mayores o iguales a cuatro.
def exp2(t):
    n = t**2
    return n
i = 0
while i < 3:
    N = input ('Ingresar un número de 4 digitos: ')
    li = len(N)
    if N.isnumeric() and li >= 4:
        N = int(N); k = str(exp2(N)); lf = len (k); dif = lf - li
        u1 = dif // 2
        v1 = u1 + li
        ale = k[u1:v1]
        print ('0,' + ale)
        i = 3
    elif i < 2:
        oportunities = 2 - i
        i += 1
        if oportunities == 1:
            word = 'intento'
        else:
            word = 'intentos'
        print ('Error en el dato ingresado. Vuelva a intentar.\nTiene {} {}.'.format(oportunities, word))
    else:
        print ('Error. Fin del programa.')
        i = 3