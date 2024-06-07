# Just using this for testing!

"""# Row and Column count
m, n, o = 2, 3, 4

# Input
lst1 = [[int(input(f"A{i}{j}: ")) for j in range(1,n+1)] for i in range(1,m+1)]
print()
lst2 = [[int(input(f"B{i}{j}: ")) for j in range(1,o+1)] for i in range(1,n+1)]
lst2 = [[lst2[j][i] for j in range(len(lst2))] for i in range(len(lst2[0]))]

# lst3 = []
# for i in range(len(lst1)):
#     lst4 = []
#     for j in range(len(lst2)):
#         sum=0
#         for k in range(len(lst2[0])):
#             sum+=lst1[i][k]*lst2[j][k]
#         lst4.append(sum)
#     lst3.append(lst4)
lst3 = [[sum([lst1[i][k]*lst2[j][k] for k in range(len(lst2[0]))]) for j in range(len(lst2))]for i in range(len(lst1))]

# Ouput
# [print(" ".join(i)) for i in [[str(j) for j in i] for i in lst2]]
print(lst1,lst2,lst3,sep="\n")
"""
# for i in range(len(lst2[0])):
#     lst4 = []
#     for j in range(len(lst2)):
#         lst4.append(lst2[j][i])
#     lst3.append(lst4)

def HelloWorld(x):
    x("HelloWorld")

HelloWorld(print)

# lst = [ [1, 2, 3],\
#         [4, 5, 6],\
#         [7, 1, 9]]
# lst.index()
# def test(lst, m=0, n=0):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         for k in range(len(lst[0])):
#             lst[0] * test([[lst[i][j] for j in range(len(i)) if (j!=m and i!=n)] for i in range(len(lst))], m+1, n+1)
    
# print(test(lst))
    
# def det(lst):
#     if len(lst) == 1:
#         return lst[0][0]
#     elif len(lst) == 2:
#         return lst[0][0]*lst[1][1] - lst[0][1]*lst[1][0]
#     else:
#         return sum([(((-1) ** c) * lst[0][c] * test_MIN(lst, 0, c)) for c in range(len(lst))])

# def min(lst, row = 0, col = 0):
#     return [[lst[r][c] for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row]

# def COF(lst, row = -1, col = -1):
#     if row == -1 and col == -1:
#         return {lst[row][col]: [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row] for row in range(len(lst)) for col in range(len(lst[row]))}
#     return [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row]

# def cof(lst, row = -1, col = -1):
#     if row == -1 and col == -1:
#         return {lst[row][col] : [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row] for row in range(len(lst)) for col in range(len(lst))}
#     return [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row]


# def MIN(lst:list, row:int = -1, col:int = -1):
#     if row == -1 and col == -1:
#         return {lst[row][col] : [[lst[r][c] for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row] for row in range(len(lst)) for col in range(len(lst))}
#     return [[lst[r][c] for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row]

# def cof(lst:list, row:int = -1, col:int = -1):
#     if row == -1 and col == -1:
#         return {lst[row][col] : [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row] for row in range(len(lst)) for col in range(len(lst))}
#     return [[(((-1) ** (r + c)) * lst[r][c]) for c in range(len(lst[r])) if c != col] for r in range(len(lst)) if r != row]


# def test_MIN(lst, row, col):
    # lst2 = []
    # for r in range(len(lst)):
    #     if r != row:
    #         lst3 = []
    #         for c in range(len(lst)):
    #             if c != col:
    #                 lst3.append(lst[r][c])
    #         lst2.append(lst3)
    # # return det(lst2)
    # return det([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row])

def TRA(lst:list):
    return [[lst[j][i] for j in range(len(lst))] for i in range(len(lst[0]))]

def MIN(lst:list, row:int = -1, col:int = -1):
    if row == -1 and col == -1:
        return [[DET([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row]) for col in range(len(lst))] for row in range(len(lst))]
    return DET([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row])

def COF(lst:list, row:int = -1, col:int = -1):
    if row == -1 and col == -1:
        return [[(((-1) ** (row + col)) * MIN(lst, row, col)) for col in range(len(lst))] for row in range(len(lst))]
    return (((-1) ** (row + col)) * MIN(lst, row, col))

def DET(lst:list):
    if len(lst) == 1:
        return lst[0][0]
    elif len(lst) == 2:
        return lst[0][0]*lst[1][1] - lst[0][1]*lst[1][0]
    else:
        return sum([((-1) ** c) * lst[0][c] * MIN(lst, row = 0, col = c) for c in range(len(lst))])

def ADJ(lst):
    return TRA(COF(lst))

def INV(lst):
    D = DET(lst)
    if D != 0:
        return [[(1/D) * col for col in row] for row in ADJ(lst)]
    else:
        raise ZeroDivisionError("\n-- Inverse Not Possible, ZeroDivisionError! --\n")

lst = [ [1, 2, 3],\
        [4, 5, 6],\
        [7, 8, 9]]
try:
    print(INV(lst))
except ZeroDivisionError as e:
    print(e)
# return [[DET([[lst[r][c] for c in range(len(lst)) if c != col] for r in range(len(lst)) if r != row]) for col in range(len(lst))] for row in range(len(lst))]

#-----------------------------------------------------------------------------#

# Hi there👋,
# This is the author speaking🗣️ :- Since you are here, keep a cookie 🍪!
# and this is just a testing area, dont need to read it all,
# it's mostly the same as the "Mfunc.py" file which has all the functions.

# If you face any issues, just open an issue at:
# https://github.com/MTCodes01/Matrix-Calculator/issues
" Don't except me to respond quickly, I may be slow to respond"
# But don't worry i will respond and help when i see the issue notification!

# Happy coding and don't hesitate to ask if there is anything on discord: mt_yt
# My github profile, if needed: https://github.com/MTCodes01
# ok then Cya👋!

#-----------------------------------------------------------------------------#