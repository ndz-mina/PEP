#Código para generar un número pseudoaleatoreo usando 
#la técnica del cuadrado medio para dígitos mayores o iguales a cuatro.

def exp2(t):
    n = t**2
    return n

def word(x):
    if x == 1:
        c = 'intento'
    else:
        c = 'intentos'
    return c

i = 1
while i < 4:
    N = input ('Ingresar un número de 4 digitos: ')
    li = len(N)

    if N.isnumeric() and li >= 4:
        N = int(N); k = str(exp2(N)); lf = len (k); dif = lf - li
        u1 = dif // 2
        v1 = u1 + li
        ale = k[u1:v1]
        print ('0,' + ale)
        i = 4

    elif i < 3:
        oportunities = 3 - i
        i += 1
        print ('Error en el dato ingresado. Vuelva a intentar.\nTienes {} {}.'.format(oportunities, word(oportunities)))
    
    else:
        print ('Error. Fin del programa.')
        i = 4