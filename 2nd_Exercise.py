#Código para determinar cuántos días se toma un caracol en recorrer una distancia.
#Para distancias pertenecientes a los números enteros y aproximando 1 día a 24 hrs.
t = 12; h_day = t; h_night = 24 - t
def time(h_day, H, dr, Ld):
    h_max = h_day * ((H - dr) / Ld)
    h = h_max // 24
    m_max = h_max % 24
    m = m_max // 60
    s = m_max % 60
    t = [h, m, s]
    return (t)
def wd(x):
    if x == 1:
        c = 'día'
    else:
        c = 'días'
    return c
def wh(x):
    if x == 1:
        c = 'hora'
    else:
        c = 'horas'
    return c
def wm(x):
    if x == 1:
        c = 'minuto'
    else:
        c = 'minutos'
    return c
def ws(x):
    if x == 1:
        c = 'segundo'
    else:
        c = 'segundos'
    return c
H = input('Ingrese cuántos metros de profundidad tiene el pozo: ')
if H.isnumeric():
    Ld = input('Ingrese cuántos metros asciende: ')
    if Ld.isnumeric():
        Ln = input('Ingrese cuántos metros desciende: ')
        if Ln.isnumeric():
            H = int(H); Ld = int(Ld); Ln = int(Ln)
            if H > Ld:
                if Ld > Ln:
                    position = [0, Ld]
                    dr = Ld
                    while dr < H:
                        dr = dr - Ln; position.append(dr)
                        dr = dr + Ld
                        if dr <= H:
                            position.append(dr)
                    d = len(position) // 2
                    dr = position[-1]; dif = time(h_day, H, dr, Ld)
                    h = dif[0]; m = dif[1]; s = dif[2]
                    if h != 0 and m != 0 and s != 0:
                        print('El caracol saldrá del pozo en {} {} con {} {}, {} {} y {} {}.'.format(d, wd(d),h, wh(h), m, wm(m), s, ws(s)))
                    elif h == 0 and m != 0 and s != 0:
                        print('El caracol saldrá del pozo en {} {} con {} {} y {} {}.'.format(d, wd(d), m, wm(m), s, ws(s)))
                    elif h != 0 and m == 0 and s != 0:
                        print('El caracol saldrá del pozo en {} {} con {} {} y {} {}.'.format(d, wd(d),h, wh(h), s, ws(s)))
                    elif h != 0 and m != 0 and s == 0:
                        print('El caracol saldrá del pozo en {} {} con {} {} y {} {}.'.format(d, wd(d),h, wh(h), m, wm(m)))
                    else:
                        print('El caracol saldrá del pozo en {} {}.'.format(d, wd(d)))
                else:
                    print('El caracol nunca saldrá del pozo.')
            elif H == Ld:
                print('El caracol sale en {} horas'.format(h_day))
            else:
                dr = 0; dif = time(h_day, H, dr, Ld)
                h = dif[0]; m = dif[1]; s = dif[2]
                print('El caracol saldrá del pozo en menos de 1 día.\nEn {} {}, {} {} y {} {} saldrá.'.format(h, wh(h), m, wm(m), s, ws(s)))
        else:
            print('Error en el valor de descenso.')
    else:
        print('Error en el valor de ascenso.')
else:
    print('Error en el valor de la profundidad.')