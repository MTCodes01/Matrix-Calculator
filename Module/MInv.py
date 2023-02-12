import Module.MDet as MDet
import Module.MAdj as MAdj
def inv11(x):
    if MDet.det11(x)==0:
        print("\nZero Division Error!\n")
        return None
    else:
        z=[]
        for i in MAdj.adj11(x):
            z.append(MDet.det11(x)*i)
        return z
def inv22(x):
    if MDet.det22(x)==0:
        print("\nZero Division Error!\n")
        return None
    else:
        z=[]
        for i in MAdj.adj22(x):
            z.append(MDet.det22(x)*i)
        return z
def inv33(x):
    if MDet.det33(x)==0:
        print("\nZero Division Error!\n")
        return None
    else:
        z=[]
        for i in MAdj.adj33(x):
            z.append(MDet.det33(x)*i)
        return z