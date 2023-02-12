def min11(x):
    z=[]
    z.append(x[0])
    return z
def min22(x):
    z=[]
    z.append(x[3])
    z.append(x[2])
    z.append(x[1])
    z.append(x[0])
    return z
def min33(x):
    z=[]
    z.append((x[4]*x[8])-(x[5]*x[7]))
    z.append((x[3]*x[8])-(x[5]*x[6]))
    z.append((x[3]*x[7])-(x[4]*x[6]))
    z.append((x[1]*x[8])-(x[2]*x[7]))
    z.append((x[0]*x[8])-(x[2]*x[6]))
    z.append((x[0]*x[7])-(x[1]*x[6]))
    z.append((x[1]*x[8])-(x[2]*x[7]))
    z.append((x[0]*x[5])-(x[2]*x[3]))
    z.append((x[0]*x[4])-(x[1]*x[3]))
    return z