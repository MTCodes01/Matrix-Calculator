import Module.MMin as MMin
def cof11(x):
    z=MMin.min11(x)
    return z
def cof22(x):
    z=MMin.min22(x)
    z[1]=-z[1]
    z[2]=-z[2]
    return z
def cof33(x):
    z=MMin.min33(x)
    z[1]=-z[1]
    z[3]=-z[3]
    z[5]=-z[5]
    z[7]=-z[7]
    return z