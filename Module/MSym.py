import Module.MTra as MTra
def sym11(x):
    return True
def sym22(x):
    z=MTra.tra22(x)
    count=0
    for i in range(len(z)):
        if x[i]==z[i]:
            count+=1
    if count==4:
        return True
    else:
        return False
def sym33(x):
    z=MTra.tra33(x)
    count=0
    for i in range(len(z)):
        if x[i]==z[i]:
            count+=1
    if count==9:
        return True
    else:
        return False