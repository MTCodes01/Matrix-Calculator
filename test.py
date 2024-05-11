"""# Row and Column count
m, n, o = 2, 3, 4

# Input
lst1 = [[int(input(f"A{i}{j}: ")) for j in range(1,n+1)] for i in range(1,m+1)]
print()
lst2 = [[int(input(f"B{i}{j}: ")) for j in range(1,o+1)] for i in range(1,n+1)]
lst2 = [[lst2[j][i] for j in range(len(lst2))] for i in range(len(lst2[0]))]

# lst3 = []
# for i in range(len(lst1)):
#     lst4 = []
#     for j in range(len(lst2)):
#         sum=0
#         for k in range(len(lst2[0])):
#             sum+=lst1[i][k]*lst2[j][k]
#         lst4.append(sum)
#     lst3.append(lst4)
lst3 = [[sum([lst1[i][k]*lst2[j][k] for k in range(len(lst2[0]))]) for j in range(len(lst2))]for i in range(len(lst1))]

# Ouput
# [print(" ".join(i)) for i in [[str(j) for j in i] for i in lst2]]
print(lst1,lst2,lst3,sep="\n")
"""
# for i in range(len(lst2[0])):
#     lst4 = []
#     for j in range(len(lst2)):
#         lst4.append(lst2[j][i])
#     lst3.append(lst4)
def HelloWorld(x):
    x("HelloWorld")

HelloWorld(print)