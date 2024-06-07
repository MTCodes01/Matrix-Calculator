# Import section
import Module.Mfunc as M

a=input("Enter \"Y\" to start!:")

#__main__
def __main__():
    while True:
        print("\n1)Addition")
        print("2)Difference")
        print("3)Multiplication")
        print("4)Transpose")
        print("5)Minor")
        print("6)Cofactor")
        print("7)Adjoint")
        print("8)Determinant") 
        print("9)Inverse")
        print("10)Exit")

        o2=input("\nEnter your option:")

        if o2=="1" or o2.lower()=="1)addition" or o2.lower()=="addition":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.ADD(M.inp(m1, n1, m1, n1)))

        elif o2=="2" or o2.lower()=="2)difference" or o2.lower()=="difference":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.SUB(M.inp(m1, n1, m1, n1)))

        elif o2=="3" or o2.lower()=="3)multiplication" or o2.lower()=="multiplication":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m1:")), int(input("n1:"))
            print(f"m2:{n1}")
            n2 = int(input("n2:"))
            M.out(M.MUL(M.inp(m1, n1, n1, n2)))

        elif o2=="4" or o2.lower()=="4)transpose" or o2.lower()=="transpose":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.TRA(M.inp(m1, n1)))

        elif o2=="5" or o2.lower()=="5)minor" or o2.lower()=="minor":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.MIN(M.inp(m1, n1)))

        elif o2=="6" or o2.lower()=="6)cofactor" or o2.lower()=="cofactor":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.COF(M.inp(m1, n1)))

        elif o2=="7" or o2.lower()=="7)adjoint" or o2.lower()=="adjoint":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.ADJ(M.inp(m1, n1)))

        elif o2=="8" or o2.lower()=="8)determinant" or o2.lower()=="determinant":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.DET(M.inp(m1, n1)))

        elif o2=="9" or o2.lower()=="9)inverse" or o2.lower()=="inverse":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            try:
                M.out(M.INV(M.inp(m1, n1)))
            except ZeroDivisionError as e:
                print(e)
            
        elif o2=="10" or o2.lower()=="10)exit" or o2.lower()=="exit":
            break
        else:
            print("\nInvalid Input!\n")

#__main__() FUNCTION CALL
if a.lower()=="y":
    try:
        __main__()
    except:
        print("\n-- ERROR --")
print("\nEXITED!")