import modulo_Mina

def valInt(var1, var2 = None):
    
    if modulo_Mina.test(var1) == "class 'int'":
        var1 = modulo_Mina.number(var1)
        
        if var2 == None:
            x = True

        else:
            type_var2 = modulo_Mina.intervals(var2)

            if (type_var2 == 'list with 2 elements' or type_var2 == 'tuple with 2 elements'):

                var2 = eval(var2)
                u = var2[0]; v = var2[1]
                t1 = modulo_Mina.test(u); t2 = modulo_Mina.test(v)

                if (t1 == "class 'int'" or t1 == "class 'float'")\
                    and (t2 == "class 'int'" or t2== "class 'float'"):
                    q = modulo_Mina.order(u, v)

                if q == 'increasing':
                    if type_var2 == 'tuple with 2 elements'\
                        and (u < var1) and (var1 < v):          #Open Interval
                        x = True

                    elif type_var2 == 'list with 2 elements'\
                        and (u <= var1) and (var1 <= v):       #Closed Interval
                        x = True

                    else:
                        x = False

                else:
                    x = ValueError

            else:
                x = TypeError
    
    else:
        x = False

    return x

def valFloat(var1, var2 = None):
    
    if modulo_Mina.test(var1) == "class 'float'":
        var1 = modulo_Mina.number(var1)
        
        if var2 == None:
            x = True

        else:
            type_var2 = modulo_Mina.intervals(var2)

            if (type_var2 == 'list with 2 elements' or type_var2 == 'tuple with 2 elements'):

                var2 = eval(var2)
                u = var2[0]; v = var2[1]
                t1 = modulo_Mina.test(u); t2 = modulo_Mina.test(v)

                if (t1 == "class 'int'" or t1 == "class 'float'")\
                    and (t2 == "class 'int'" or t2== "class 'float'"):
                    q = modulo_Mina.order(u, v)

                if q == 'increasing':
                    if type_var2 == 'tuple with 2 elements'\
                        and (u < var1) and (var1 < v):          #Open Interval
                        x = True

                    elif type_var2 == 'list with 2 elements'\
                        and (u <= var1) and (var1 <= v):       #Closed Interval
                        x = True

                    else:
                        x = False

                else:
                    x = ValueError

            else:
                x = TypeError
    
    else:
        x = False

    return x

def valComplex(var1, var2 = None):
    
    if modulo_Mina.test(var1) == "class 'complex'":
        var1 = modulo_Mina.number(var1)
        
        if var2 == None:
            x = True

        else:
            type_var2 = modulo_Mina.intervals(var2)

            if (type_var2 == 'list with 2 elements' or type_var2 == 'tuple with 2 elements'):

                var2 = eval(var2)
                u = var2[0]; v = var2[1]
                t1 = modulo_Mina.test(u); t2 = modulo_Mina.test(v)

                if (t1 == "class 'int'" or t1 == "class 'float'")\
                    and (t2 == "class 'int'" or t2== "class 'float'"):
                    q = modulo_Mina.order(u, v)

                if q == 'increasing':
                    if type_var2 == 'tuple with 2 elements'\
                        and (u < var1) and (var1 < v):          #Open Interval
                        x = True

                    elif type_var2 == 'list with 2 elements'\
                        and (u <= var1) and (var1 <= v):       #Closed Interval
                        x = True

                    else:
                        x = False

                else:
                    x = ValueError

            else:
                x = TypeError
    
    else:
        x = False

    return x

def valList(var1, var2 = None, var3 = None):

    if modulo_Mina.test(var1) == "class 'list'":
        var1 = eval(var1)
        t = len(var1)

        if var2 == None and var3 == None:
            x = True

        elif (var2 != None) and (var3 != None):

            if modulo_Mina.test(var3) == "class 'str'":

                if var3 == 'len' or var3 == 'value':

                    if var3 == 'len' and modulo_Mina.test(var2) == "class 'int'":
                        var2 = int(var2)
                    
                        if t == var2:
                            x = True

                    elif var3 == 'value' and modulo_Mina.test(var2) == "class 'list'":
                        var2 = eval(var2)

                        if var1 == var2:
                            x = True

                    else:
                        x = False

                else:
                    x = ValueError

            else:
                x = TypeError
        
        else:
            x = TypeError
        
    else:
        x = False

    return x
