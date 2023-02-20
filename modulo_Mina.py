def sequence(var, element):

    var = str(var); element = str(element)
    p = var.find(element)

    if p != -1:

        list_var = []

        for i in var:
            list_var.append(i)

        j = len(list_var); count = 0

        for u in range (0,j):
            if list_var[u] == element and list_var[u+1] == element:
                count += 1

        if count == 0:
            c = 'No sequence'

        else:
            c = 'Sequence'

    else:
        c = ValueError

    return c

def test_tuple(var):

    t = str(var); p = len(t)

    if (p >= 3) and (t[0] == '(') and (t[-1] == ')'):            #List
        try:
            x = eval(t)
            sequence(t, ',') == 'No sequence'
        
        except:
            x = 'No valid'

        else:
            x = "class 'tuple'"

    else:
        x = 'Non tuple'

    return(x)

def test_num(n):

    t = str(n); num = 0; point = 0; add = 0; rest = 0; im = 0; alf = 0

    for i in t:
        
        if i.isnumeric():
            num += 1
        elif i == '.':
            point += 1
        elif i == '+':
            add += 1; u = t.find('+')
        elif i == '-':
            rest += 1; u = t.find('-')
        elif i.isalpha():
            if i == 'j':
                im += 1
            else:
                alf += 1

    if (alf == 0) and (point <= 2) and (add <= 1) and (rest <= 2) and (im <= 1):                      #Set of Numbers

        if num == len(t) or (rest == 1 and num == (len(t) - 1)):                                      #Integer Numbers
            x = "class 'int'"

        elif ((num + point) == len(t) or (rest == 1 and (num + point) == (len(t) - 1)))\
            and point == 1 and (t[0] != '.' or t[-1] != '.'):                                         #Float Numbers
            x = "class 'float'"

        elif (len(t) >= 2) and (im == 1) and ((t[-1] == 'j' and (t[0] != '+' 
            or t[-2] != '+' or t[-2] != '-') and (t[0] != '.' or t[-2] != '.' 
            or t[u-1] != '.' or t[u+1] != '.')) or (t[u-1] == 'j' and (t[0] != '+'
            or t[-1] != '+' or t[-1] != '-') and (t[0] != '.' or t[-1] != '.' 
            or t[u-2] != '.' or t[u+1] != '.'))) and not (add == 1 and rest == 2):                     #Complex Numbers
            x = "class 'complex'"

        else:
            x = "class 'str'"

    else:
        x = "class 'str'"

    return x

def test_list(var):

    t = str(var); p = len(t)

    if (p >= 3) and (t[0] == '[') and (t[-1] == ']'):            #List
        try:
            x = eval(t)
            sequence(t, ',') == 'No sequence'
        
        except:
            x = 'No valid'

        else:
            x = "class 'list'"
    
    else:
        x = 'Non list'

    return(x)

def test(var):
    if test_list(var) == "class 'list'":
        x = "class 'list'"

    elif test_tuple(var) == "class 'tuple'":
        x = "class 'tuple'"

    else:
        x = test_num(var)
        
    return x

def number(var):
    t_num = test_num(var)
    if t_num == "class 'int'":
        var = int(var)

    elif t_num == "class 'float'":
        var = float(var)
        
    elif t_num == "class 'complex'":
        var = complex(var)
    
    return var

def order(var1, var2):

    var1 = number(var1); var2 = number(var2)
    
    if var1 < var2:
        x = 'increasing'
    else:
        x = 'decreasing'

    return x

def intervals(var):
    t = test(var)

    if t == "class 'list'" or t == "class 'tuple'":

        var = eval(var)
        v = len(var)

        if v == 2 and t == "class 'list'":
            x = 'list with 2 elements'

        elif v == 2 and t == "class 'tuple'":
            x = 'tuple with 2 elements'

    else:
        x = TypeError

    return x

def test_matrix(M):

    if test(M) == "class 'list'":
        
        M = eval(M)
        row = len(M)
        column = 0
        count_list = 0
        for i in range(row):
            r1 = len(M[i])
            if r1 > column:
                column = r1
            if test(M[i])== "class 'list'":
                count_list += 1

        count_column = 0
        for i in range(row):
            if len(M[i]) == column:
                count_column += 1

        count_elements = 0
        for i in range(row):
            for j in range(column):
                if (test(M[i][j]) == "class 'int'") or (test(M[i][j]) == "class 'float'")\
                    or (test(M[i][j]) == "class 'complex'"):
                    count_elements += 1

        if (count_column == row) and (count_list == row) and (row >= 1) and (column >= 1)\
            and (count_elements == (row * column)) and not (row == 1 and column == 1):
            x = 'Valid'

        else:
            x = 'No valid'

    else:
        x = 'No matrix'

    return x

def len_matrix(M):

    if test_matrix(M) == 'Valid':

        M = eval(M)
        x = (len(M), len(M[0]))

    else:
        x = TypeError

    return x

def identy_matrix(m):

    if test_num(m) == "class 'int'":
        m = int(m)

        if m > 1:
            I = []

            for i in range(m):
                row = []

                for j in range(m):

                    if i == j:
                        row.append(1)

                    else:
                        row.append(0)

                I.append(row)
            x = I
        
        else:
            x = ValueError
    
    else:
        x = TypeError
    
    return x

def ec_to_matrix(ec):
    pass