#Linear search 
# s=int(input("enter the elememt size of the list"))
# nums=[]
# for e in range(s):
#     ele=int(input("enter the elememt in the list"))
#     nums.append(ele) 
# print(nums)     
# n=int(input("enter the elememt to search in the list"))
# for i in nums:
#     if n==i:
#         print(f"the {n} was found in the list at index of:",i)
#         break
# else:
#     print(f"{n} was not found in the list")    

#Linear Search using the methods
pos=-1
def search(list,n):
    for i in list:
        if n==i:
            global pos
            pos=i
            return True
         
list=[1,2,3,4,5,6]
n=60
if search(list,n):
    print("it is found",pos)
else:
    print("it is not found")   



    
    