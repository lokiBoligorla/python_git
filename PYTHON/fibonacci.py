# def fibi(n):
#     a=0
#     b=1
#     if n==1:
#         print(a)
#     elif n<0:
#         print("only positive values")
#     else:    
#           print(a)
#           print(b)
#           for i in range(2,n):
#             c=a+b
#             a=b
#             b=c 
#             print(c)
# fibi(530)            


n=int(input("enter the number"))
a=0
b=1
print(a)
print(b)
for i in range(2,n):
    c=a+b
    a=b
    b=c
    print(c)
