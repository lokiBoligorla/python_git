# from sys import *
# setrecursionlimit(1002)
# i=0
# def name():
#     global i
#     i+=1
#     print("lokesh",i)
#     name()
# name()    


def fact(x):
    if x==0:
        return 1
    return x*fact(x-1)

result=fact(5)
print(result)
   