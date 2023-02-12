import Module.MTra as MTra
def ske11(x):
    if x[0]==0:
        return True
    else:
        return False
def ske22(x):
    z=MTra.tra22(x)
    count=0
    if x[0]==0:
            count+=1
    if x[3]==0:
            count+=1
    if x[1]==-z[1]:
            count+=1
    if x[2]==-z[2]:
            count+=1
    if count==4:
        return True
    else:
        return False
def ske33(x):
    z=MTra.tra33(x)
    count=0
    for i in range(1,8,2):
        if x[i]==-z[i]:
            count+=1
    for i in range(2,7,4):
        if x[i]==-z[i]:
            count+=1
    if x[0]==0:
            count+=1
    if x[4]==0:
            count+=1
    if x[8]==0:
            count+=1
    if count==9:
        return True
    else:
        return False