pos=-1
def search(list,n):
    l=0
    u=len(list)-1

    while l<=u:
        mid=(l+u)//2

        if list[mid]==n:
            global pos
            pos=mid
            return True
        else:
            if list[mid]< n:
                l=mid+1
            else:
                u=mid-1   
    return False         

list=[3,5,7,3,2,4,6,8,990,12]
list=sorted(list)
print(list)
n=8
if search(list,n):
    print("it is found",pos+1)
else:
    print("not found")    
                   




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
#             if mid<n:
#                 l=mid
#             else:
#                 u=mid
#     return False            

# list=[1,2,3,4,5,6,7,8,9,10]
# n=70

# if search(list,n):
#     print("found")
# else:
#     print("not found") 


