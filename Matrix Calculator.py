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

        elif o2=="5" or o2.lower()=="5)minor" or o2.lower()=="minor":                      #THIS IS INVOKED IF THE INPUT WAS "5)Minor"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=i.min11(lst1)
                print(' ')
                print(x)
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=i.min22(lst1)
                print(' ')
                print('[',x[0],'',x[1],'\n ',x[2],'',x[3],']')
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=i.min33(lst1)
                print(' ')
                print('[',x[0],'',x[1],'',x[2],'\n ',x[3],'',x[4],'',x[5],'\n ',x[6],'',x[7],'',x[8],']')
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="6" or o2.lower()=="6)cofactor" or o2.lower()=="cofactor":                #THIS IS INVOKED IF THE INPUT WAS "6)Cofactor"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=j.cof11(lst1)
                print(' ')
                print(x)
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=j.cof22(lst1)
                print(' ')
                print('[',x[0],'',x[1],'\n ',x[2],'',x[3],']')
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=j.cof33(lst1)
                print(' ')
                print('[',x[0],'',x[1],'',x[2],'\n ',x[3],'',x[4],'',x[5],'\n ',x[6],'',x[7],'',x[8],']')
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="7" or o2.lower()=="7)adjoint" or o2.lower()=="adjoint":                  #THIS IS INVOKED IF THE INPUT WAS "7)Adjoint"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=k.adj11(lst1)
                print(' ')
                print(x)
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=k.adj22(lst1)
                print(' ')
                print('[',x[0],'',x[1],'\n ',x[2],'',x[3],']')
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=k.adj33(lst1)
                print(' ')
                print('[',x[0],'',x[1],'',x[2],'\n ',x[3],'',x[4],'',x[5],'\n ',x[6],'',x[7],'',x[8],']')
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="8" or o2.lower()=="8)symmetric" or o2.lower()=="symmetric":              #THIS IS INVOKED IF THE INPUT WAS "8)Symmetric"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=l.sym11(lst1)
                if x==True:
                    print('\nThe given matrix is a Symmetric matrix\n')
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=l.sym22(lst1)
                if x==True:
                    print('\nThe given matrix is a Symmetric matrix\n')
                else:
                    print("\nThe given matrix is not a Symmetric matrix\n")
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=l.sym33(lst1)
                if x==True:
                    print('\nThe given matrix is a Symmetric matrix\n')
                else:
                    print("\nThe given matrix is not a Symmetric matrix\n")
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="9"or o2.lower()=="9)skew symmetric" or o2.lower()=="skew symmetric":     #THIS IS INVOKED IF THE INPUT WAS "9)Skew Symmetric"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=m.ske11(lst1)
                if x==True:
                    print('\nThe given matrix is a skew Symmetric matrix\n')
                else:
                    print("\nThe given matrix is not a skew Symmetric matrix\n")
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=m.ske22(lst1)
                if x==True:
                    print('\nThe given matrix is a skew Symmetric matrix\n')
                else:
                    print("\nThe given matrix is not a skew Symmetric matrix\n")
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=m.ske33(lst1)
                if x==True:
                    print('\nThe given matrix is a skew Symmetric matrix\n')
                else:
                    print("\nThe given matrix is not a skew Symmetric matrix\n")
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="10" or o2.lower()=="10)determinant" or o2.lower()=="determinant":        #THIS IS INVOKED IF THE INPUT WAS "10)Determinant"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=n.det11(lst1)
                print("\t",x)
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=n.det22(lst1)
                print("\t",x)
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=n.det33(lst1)
                print("\t",x)
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="11" or o2.lower()=="11)inverse" or o2.lower()=="inverse":                #THIS IS INVOKED IF THE INPUT WAS "11)Inverse"
            print(' ')
            print("Type 'm' by 'n' order of your Matrix(max:3 by 3).")
            m1=eval(input("m:"))
            n1=eval(input("n:"))
            if m1==1 and n1==1:
                print(' ')
                a11=eval(input("a11:"))
                lst1=[a11]
                x=o.inv11(lst1)
                print(' ')
                if x!=None:
                    print(x)
                lst1.clear()
            elif m1==2 and n1==2:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                lst1=[a11,a12,a21,a22]
                x=o.inv22(lst1)
                print(' ')
                if x!=None:
                    print('[',x[0],'',x[1],'\n ',x[2],'',x[3],']')
                lst1.clear()
            elif m1==3 and n1==3:
                print(' ')
                a11=eval(input("a11:"))
                a12=eval(input("a12:"))
                a13=eval(input("a13:"))
                a21=eval(input("a21:"))
                a22=eval(input("a22:"))
                a23=eval(input("a23:"))
                a31=eval(input("a31:"))
                a32=eval(input("a32:"))
                a33=eval(input("a33:"))
                lst1=[a11,a12,a13,a21,a22,a23,a31,a32,a33]
                x=o.inv33(lst1)
                print(' ')
                if x!=None:
                    print('[',x[0],'',x[1],'',x[2],'\n ',x[3],'',x[4],'',x[5],'\n ',x[6],'',x[7],'',x[8],']')
                lst1.clear()
            else:
                print("Only inputs allowed are 1 by 1 , 2 by 2 and 3 by 3!")
        elif o2=="12" or o2.lower()=="12)exit" or o2.lower()=="exit":                      #THIS IS INVOKED IF THE INPUT WAS "12)Exit"
            print("\nSUCCESSFULLY EXITED!")
            print("====================")
            break
        else:                                                                              #THIS IS INVOKED IF THE INPUT WAS NOT CORRECT
            print("\nInvalid Input!\n")

#__main__() FUNCTION CALL
if a.lower()=="y":
    try:
        __main__()
    except:
        print("\n!ERROR!\n\nEXITED")
else:
    print("\nExited!\n")