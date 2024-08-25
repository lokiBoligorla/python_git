# n=5
# for i in range(5):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()  
# for i in range(5):
#     for j in range((n-1)-i):
#         print("*",end=" ")
#     print() 


# def star_triangle(n):
#     for i in range(n):
#         print(" "*(n-1-i),end="  ") 
#         print("*"*((i*2)+1)) 
# star_triangle(5)  

n=10
for i in range(n):
   
    for j in range(n-i):
        print(" ",end=" ")     
    for j in range(i+1):
         print("*",end=" ")
     
    for j in range(i):
         print("*",end=" ")   
   
    print()
           
         




