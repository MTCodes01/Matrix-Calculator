#IMPORT SECTION!
from time import sleep
import Module.Mfunc as M

# #PRINT COMMENT SECTION!
# print("!Before you start with the calculations,READ THIS!\n\
# For understanding this program you need to atleast know about Matrix's and Determinant's!\n\
# I made this program Imagining this structure in mind:\n\
#             \t[  a11    a12    a13\n\
#             \t   a21    a22    a23\n\
#             \t   a31    a32    a33  ]\n\
#             \t\t  AND\n\
#             \t[  b11    b12    b13\n\
#             \t   b21    b22    b23\n\
#             \t   b31    b32    b33  ]\n\
# Which limits at 3 by 3,if u put input of the order above that,it will exit itself!")

# #FOR DELAY!
# sleep(5)
# print("Now you can start if you understand what this is:")
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
        print("8)Symmetric")
        print("9)Skew Symmetric")
        print("10)Determinant") 
        print("11)Inverse")
        print("12)Exit")
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

        elif o2=="8" or o2.lower()=="8)symmetric" or o2.lower()=="symmetric":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.SYM(M.inp(m1, n1)))

        elif o2=="9"or o2.lower()=="9)skew symmetric" or o2.lower()=="skew symmetric":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.SKE(M.inp(m1, n1)))

        elif o2=="10" or o2.lower()=="10)determinant" or o2.lower()=="determinant":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.DET(M.inp(m1, n1)))

        elif o2=="11" or o2.lower()=="11)inverse" or o2.lower()=="inverse":
            print("\nType 'm' by 'n' order of your Matrix: ")
            m1, n1 = int(input("m:")), int(input("n:"))
            M.out(M.INV(M.inp(m1, n1)))

        elif o2=="12" or o2.lower()=="12)exit" or o2.lower()=="exit":
            print("\nSUCCESSFULLY EXITED!")
            break
        else:
            print("\nInvalid Input!\n")

#__main__() FUNCTION CALL
if a.lower()=="y":
    try:
        __main__()
    except:
        print("\n!ERROR!","INVALID INPUT","EXITED")
else:
    print("\nExited!\n")