# import math as m 
# n=int(input("enter the you want"))
# print(f"the factirial of {n} is",m.factorial(n))


# n=int(input("enter the number"))
# f=1
# for i in range(1,n+1):
#     f=f*i
# print(f)

x=int(input("enter the number"))
def fact(x):
    f=1
    for i in range(2,x+1):
        f*=i
    print(f)    
fact(x)


