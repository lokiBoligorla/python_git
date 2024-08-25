# from array import *
# demo=array("i",[])
# x=int(input("enter the length of the array "))

# for i in range(x):
#     new=int(input("enter the elements in array "))
#     demo.append(new)
# print(demo)  

# particular_ele=int(input("enter th element do you want to search "))
# for e in demo:
#     if particular_ele==e:
#         print("index is",demo.index(particular_ele))
#         break
# else:
#     print("element was not found ")   

from array import *
arr=array("i",[]) 
n=int(input("enter the size array1"))
sum=0
for i in range(n):
    ele=int(input("enter the ele of array1"))
    arr.append(ele)
print(arr) 

arr1=array("i",[]) 
n=int(input("enter the size array2"))
sum=0
for i in range(n):
    ele=int(input("enter the ele of array2"))
    arr1.append(ele)
print(arr1) 
arr3=arr+arr1
sum_of_two_arrays=0
for num in arr3:
    sum_of_two_arrays+=i

print("the sum of two arrays",sum_of_two_arrays)
      


