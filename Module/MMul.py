"""
FUNCTIONS IN THIS CODE:

!USE Module.MMul.<function_name>()

MATRIX MULTIPLICATION:
 mul11,mul22,mul33
"""
def mul11(x,y):                                  # n1=m2=1
    z=[]
    if len(x)==1:                                #1 BY 1 for x
        if len(y)==1:                            #1 BY 1 for y
            z.append(x[0]*y[0])
            return z
        elif len(y)==2:                          #1 BY 2 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            return z
        elif len(y)==3:                          #1 BY 3 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            z.append(x[0]*y[2])
            return z
    elif len(x)==2:                              #2 BY 1 for x
        if len(y)==1:                            #1 BY 1 for y
            z.append(x[0]*y[0])
            z.append(x[1]*y[0])
            return z
        elif len(y)==2:                          #1 BY 2 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            z.append(x[1]*y[0])
            z.append(x[1]*y[1])
            return z
        elif len(y)==3:                          #1 BY 3 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            z.append(x[0]*y[2])
            z.append(x[1]*y[0])
            z.append(x[1]*y[1])
            z.append(x[1]*y[2])
            return z
    elif len(x)==3:                              #3 BY 1 for x
        if len(y)==1:                            #1 BY 1 for y
            z.append(x[0]*y[0])
            z.append(x[1]*y[0])
            z.append(x[2]*y[0])
            return z
        elif len(y)==2:                          #1 BY 2 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            z.append(x[1]*y[0])
            z.append(x[1]*y[1])
            z.append(x[2]*y[0])
            z.append(x[2]*y[1])
            return z
        elif len(y)==3:                          #1 BY 3 for y
            z.append(x[0]*y[0])
            z.append(x[0]*y[1])
            z.append(x[0]*y[2])
            z.append(x[1]*y[0])
            z.append(x[1]*y[1])
            z.append(x[1]*y[2])
            z.append(x[2]*y[0])
            z.append(x[2]*y[1])
            z.append(x[2]*y[2])
            return z

def mul22(x,y):                                  # n1=m2=2
    z=[]
    if len(x)==2:                                #1 BY 2 for x
        if len(y)==2:                            #2 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1]))
            return z
        elif len(y)==4:                          #2 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2]))
            z.append((x[0]*y[1])+(x[1]*y[3]))
            return z
        elif len(y)==6:                          #2 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3]))
            z.append((x[0]*y[1])+(x[1]*y[4]))
            z.append((x[0]*y[2])+(x[1]*y[5]))
            return z
    elif len(x)==4:                              #2 BY 2 for x
        if len(y)==2:                            #2 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1]))
            z.append((x[2]*y[0])+(x[3]*y[1]))
            return z
        elif len(y)==4:                          #2 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2]))
            z.append((x[0]*y[1])+(x[1]*y[3]))
            z.append((x[2]*y[0])+(x[3]*y[2]))
            z.append((x[2]*y[1])+(x[3]*y[3]))
            return z
        elif len(y)==6:                          #2 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3]))
            z.append((x[0]*y[1])+(x[1]*y[4]))
            z.append((x[0]*y[2])+(x[1]*y[5]))
            z.append((x[2]*y[0])+(x[3]*y[3]))
            z.append((x[2]*y[1])+(x[3]*y[4]))
            z.append((x[2]*y[2])+(x[3]*y[5]))
            return z
    elif len(x)==6:                              #3 BY 2 for x
        if len(y)==2:                            #2 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1]))
            z.append((x[2]*y[0])+(x[3]*y[1]))
            z.append((x[4]*y[0])+(x[5]*y[1]))
            return z
        elif len(y)==4:                          #2 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2]))
            z.append((x[0]*y[1])+(x[1]*y[3]))
            z.append((x[2]*y[0])+(x[3]*y[2]))
            z.append((x[2]*y[1])+(x[3]*y[3]))
            z.append((x[4]*y[0])+(x[5]*y[2]))
            z.append((x[4]*y[1])+(x[5]*y[3]))
            return z
        elif len(y)==6:                          #2 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3]))
            z.append((x[0]*y[1])+(x[1]*y[4]))
            z.append((x[0]*y[2])+(x[1]*y[5]))
            z.append((x[2]*y[0])+(x[3]*y[3]))
            z.append((x[2]*y[1])+(x[3]*y[4]))
            z.append((x[2]*y[2])+(x[3]*y[5]))
            z.append((x[4]*y[0])+(x[5]*y[3]))
            z.append((x[4]*y[1])+(x[5]*y[4]))
            z.append((x[4]*y[2])+(x[5]*y[5]))
            return z

def mul33(x,y):                                  # n1=m2=3
    z=[]
    if len(x)==3:                                #1 BY 3 for x
        if len(y)==3:                            #3 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1])+(x[2]*y[2]))
            return z
        elif len(y)==6:                          #3 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2])+(x[2]*y[4]))
            z.append((x[0]*y[1])+(x[1]*y[3])+(x[2]*y[5]))
            return z
        elif len(y)==9:                          #3 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3])+(x[2]*y[6]))
            z.append((x[0]*y[1])+(x[1]*y[4])+(x[2]*y[7]))
            z.append((x[0]*y[2])+(x[1]*y[5])+(x[2]*y[8]))
            return z
    elif len(x)==6:                              #2 BY 3 for x
        if len(y)==3:                            #3 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1])+(x[2]*y[2]))
            z.append((x[3]*y[0])+(x[4]*y[1])+(x[5]*y[2]))
            return z
        elif len(y)==6:                          #3 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2])+(x[2]*y[4]))
            z.append((x[0]*y[1])+(x[1]*y[3])+(x[2]*y[5]))
            z.append((x[3]*y[0])+(x[4]*y[2])+(x[5]*y[4]))
            z.append((x[3]*y[1])+(x[4]*y[3])+(x[5]*y[5]))
            return z
        elif len(y)==9:                          #3 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3])+(x[2]*y[6]))
            z.append((x[0]*y[1])+(x[1]*y[4])+(x[2]*y[7]))
            z.append((x[0]*y[2])+(x[1]*y[5])+(x[2]*y[8]))
            z.append((x[3]*y[0])+(x[4]*y[3])+(x[5]*y[6]))
            z.append((x[3]*y[1])+(x[4]*y[4])+(x[5]*y[7]))
            z.append((x[3]*y[2])+(x[4]*y[5])+(x[5]*y[8]))
            return z
    elif len(x)==6:                              #3 BY 3 for x
        if len(y)==3:                            #3 BY 1 for y
            z.append((x[0]*y[0])+(x[1]*y[1])+(x[2]*y[2]))
            z.append((x[3]*y[0])+(x[4]*y[1])+(x[5]*y[2]))
            z.append((x[0]*y[0])+(x[1]*y[1])+(x[2]*y[2]))
            return z
        elif len(y)==6:                          #3 BY 2 for y
            z.append((x[0]*y[0])+(x[1]*y[2])+(x[2]*y[4]))
            z.append((x[0]*y[1])+(x[1]*y[3])+(x[2]*y[5]))
            z.append((x[3]*y[0])+(x[4]*y[2])+(x[5]*y[4]))
            z.append((x[3]*y[1])+(x[4]*y[3])+(x[5]*y[5]))
            z.append((x[6]*y[0])+(x[7]*y[2])+(x[8]*y[4]))
            z.append((x[6]*y[1])+(x[7]*y[3])+(x[8]*y[5]))
            return z
        elif len(y)==9:                          #3 BY 3 for y
            z.append((x[0]*y[0])+(x[1]*y[3])+(x[2]*y[6]))
            z.append((x[0]*y[1])+(x[1]*y[4])+(x[2]*y[7]))
            z.append((x[0]*y[2])+(x[1]*y[5])+(x[2]*y[8]))
            z.append((x[3]*y[0])+(x[4]*y[3])+(x[5]*y[6]))
            z.append((x[3]*y[1])+(x[4]*y[4])+(x[5]*y[7]))
            z.append((x[3]*y[2])+(x[4]*y[5])+(x[5]*y[8]))
            z.append((x[6]*y[0])+(x[7]*y[3])+(x[8]*y[6]))
            z.append((x[6]*y[1])+(x[7]*y[4])+(x[8]*y[7]))
            z.append((x[6]*y[2])+(x[7]*y[5])+(x[8]*y[8]))
            return z