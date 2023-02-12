def det11(x):
    return (x[0])
def det22(x):
    return (x[0]*x[3])-(x[1]*x[2])
def det33(x):
    return (x[0]*((x[4]*x[8])-(x[5]*x[7])))-(x[1]*((x[3]*x[8])-(x[5]*x[6])))+(x[2]*((x[3]*x[7])-(x[4]*x[6])))