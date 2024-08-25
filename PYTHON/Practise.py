#linear search
# def search(list,n):
#     for i in list:
#         if n==i:
#             return True
        
#     return False    

# list=[1,2,3,4,5,67,8]
# n=10
# if search(list,n):
#     print("it is found")
# else:
#     print('it is not found')    


# #linear search
# s=int(input("enter the size of the list"))
# list=[]
# for i in range(s):
#     ele=int(input("enter the elements of the list"))
#     list.append(ele)
# print(list)  

# n=int(input("enter the ele to search in the list"))

# for i in list:
#     if n==i:
#         print("found")
#         break
# print("not found")




#Binary Search
# pos=-1
# def search(list,n):
#     l=0
#     u=len(list)-1
#     while l<=u:
#         mid=(l+u)//2
#         if list[mid]==n:
#             global pos
#             pos=mid
#             return True
#         else:
#             if list[mid]<n:
#                 l=mid
#             else:
#                 u=mid    
#     return False
# list=[1,2,3,4,5,6,7,8,20,2,55,100,89]
# n=100
# if search(list,n):
#     print("it is found",pos+1)
# else:
#     print("not found")    
                

# Bubble sort
def sort(list):
    for i in range(len(list)-1,0,-1):
        for j in range(i):
            if list[j]>list[j+1]:
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
list=[33,41,12,78,1,0,23,100,500,250,900]                
sort(list)
print(list)
