"""
FUNCTIONS IN THIS CODE:

!USE Module.MTra.<function_name>()

MATRIX MULTIPLICATION:
 tra11,tra12,tra13
 tra21,tra22,tra23
 tra31,tra32,tra33
"""
def tra11(x):
    z=[]
    z.append(x[0])
    return z
def tra12(x):
    z=[]
    z.append(x[0])
    z.append(x[1])
    return z
def tra13(x):
    z=[]
    z.append(x[0])
    z.append(x[1])
    z.append(x[2])
    return z
def tra21(x):
    z=[]
    z.append(x[0])
    z.append(x[1])
    return z
def tra22(x):
    z=[]
    z.append(x[0])
    z.append(x[2])
    z.append(x[1])
    z.append(x[3])
    return z
def tra23(x):
    z=[]
    z.append(x[0])
    z.append(x[3])
    z.append(x[1])
    z.append(x[4])
    z.append(x[2])
    z.append(x[5])
    return z
def tra31(x):
    z=[]
    z.append(x[0])
    z.append(x[1])
    z.append(x[2])
    return z
def tra32(x):
    z=[]
    z.append(x[0])
    z.append(x[2])
    z.append(x[4])
    z.append(x[1])
    z.append(x[3])
    z.append(x[5])
    return z
def tra33(x):
    z=[]
    z.append(x[0])
    z.append(x[3])
    z.append(x[6])
    z.append(x[1])
    z.append(x[4])
    z.append(x[7])
    z.append(x[2])
    z.append(x[5])
    z.append(x[8])
    return z