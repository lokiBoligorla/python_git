def sort(lst):
 even=0
 odd=0
 for i in lst:
  if i%2==0:
   even+=1
  else:
   odd+=1
 return even,odd    
   
  
n=int(input("enter the size of the list"))
lst=[]
for i in range(n):       
 ele=int(input("enter the list elements"))
 lst.append(ele)

print(lst)    
               