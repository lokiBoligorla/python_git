# from functools import *
# lst=[1,2,3,4,56,7,8,7,63,22,3,80]
# even=list(filter(lambda a:a%2==0,lst))
# print("even",even)
# double=list(map(lambda n:n*2,lst))
# print("double",double)
# sum=reduce(lambda i,j:i+j,lst)
# print("sum",sum)



items=["lokesh",30,"hyd",890]

names=list(filter(lambda i:isinstance(i,str),items))
numbers=list(filter(lambda i:isinstance(i,(int,float)),items))
print(numbers)
print(names)


status=input("enter the martial status of person")
numbers=["lokesh","rakesh","raghu","hii"]
seperate_numbedrs1=list(map(lambda i:i+f"{status}",numbers))
seperate_numbedrs2=list(filter(lambda i:len(i)>=5,numbers))
print(seperate_numbedrs1)
print(seperate_numbedrs2)
