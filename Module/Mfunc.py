def inp(m1:int, n1:int, m2:int=0, n2:int=0):
    if m2!=0 and n2!=0:
        return ([[int(input(f"A{i}{j}: ")) for j in range(1,n1+1)] for i in range(1,m1+1)],\
            [[int(input(f"B{i}{j}: ")) for j in range(1,n2+1)] for i in range(1,m2+1)])
    else:
        return [[int(input(f"A{i}{j}: ")) for j in range(1,n1+1)] for i in range(1,m1+1)]

def out(lst:list[list[int]]):
    print()
    [print(" ".join(i)) for i in [[str(j) for j in i] for i in lst]]

def ADD(T:tuple[list[list[int]], list[list[int]]]):
    lst1, lst2 = T
    return [[lst1[i][j]+lst2[i][j] for j in range(len(lst1[0]))] for i in range(len(lst1))]

def SUB(T:tuple[list[list[int]], list[list[int]]]):
    lst1, lst2 = T
    return [[lst1[i][j]-lst2[i][j] for j in range(len(lst1[0]))] for i in range(len(lst1))]

def MUL(T:tuple[list[list[int]], list[list[int]]]):
    lst1, lst2 = T
    lst2 = TRA(lst2)
    return [[sum([lst1[i][k]*lst2[j][k] for k in range(len(lst2[0]))]) for j in range(len(lst2))]for i in range(len(lst1))]

def TRA(lst:list[list[int]]):
    return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

def MIN(lst:list[list[int]], row:int = -1, col:int = -1):
    if row == -1 and col == -1:
        return [[DET([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row]) for col in range(len(lst))] for row in range(len(lst))]
    return DET([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row])

def COF(lst:list[list[int]], row:int = -1, col:int = -1):
    if row == -1 and col == -1:
        return [[(((-1) ** (row + col)) * MIN(lst, row, col)) for col in range(len(lst))] for row in range(len(lst))]
    return (((-1) ** (row + col)) * MIN(lst, row, col))

def DET(lst:list[list[int]]):
    if len(lst) == 1:
        return lst[0][0]
    elif len(lst) == 2:
        return lst[0][0]*lst[1][1] - lst[0][1]*lst[1][0]
    else:
        return (sum([((-1) ** c) * lst[0][c] * MIN(lst, row = 0, col = c) for c in range(len(lst))]))

def ADJ(lst:list[list[int]]):
    return TRA(COF(lst))

def INV(lst:list[list[int]]):
    D = DET(lst)
    if D != 0:
        return [[(1/D) * col for col in row] for row in ADJ(lst)]
    else:
        raise ZeroDivisionError("\n-- Inverse Not Possible, ZeroDivisionError! --")
