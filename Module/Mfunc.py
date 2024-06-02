def inp(m1, n1, m2=0, n2=0):
    if m2!=0 and n2!=0:
        return [[int(input(f"A{i}{j}: ")) for j in range(1,n1+1)] for i in range(1,m1+1)],\
            [[int(input(f"B{i}{j}: ")) for j in range(1,n2+1)] for i in range(1,m2+1)]
    else:
        return [[int(input(f"A{i}{j}: ")) for j in range(1,n1+1)] for i in range(1,m1+1)]

def out(lst):
    print()
    [print(" ".join(i)) for i in [[str(j) for j in i] for i in lst]]

def ADD(T):
    lst1, lst2 = T
    return [[lst1[i][j]+lst2[i][j] for j in range(len(lst1[0]))] for i in range(len(lst1))]

def SUB(T):
    lst1, lst2 = T
    return [[lst1[i][j]-lst2[i][j] for j in range(len(lst1[0]))] for i in range(len(lst1))]

def MUL(T):
    lst1, lst2 = T
    lst2 = TRA(lst2)
    return [[sum([lst1[i][k]*lst2[j][k] for k in range(len(lst2[0]))]) for j in range(len(lst2))]for i in range(len(lst1))]

def TRA(lst):
    return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

def MIN(lst):
    return

def DET(lst): # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    return