# from numpy import *
# from sympy import Matrix
# r=int(input("enter the size of the rows"))
# c=int(input("enter the size of the colum"))

# m=[]
# for i in range(r):
#     l=[]
#     for j in range(c):
#         v=int(input("enter the elememts in matrix"))
#         l.append(v)
#     m.append(l)

# print(m)     




from numpy import *
m1=matrix("1 2 3; 4 5 6; 7 8 9")
sum=0
for i in m1:
    sum+=i
print(sum)    

     
print(m1) 
   




