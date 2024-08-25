lst=[]
n=int(input("enter the size of the list"))
even=0
odd=0
for i in range(n):
    ele=int(input("enter the elements of the list"))
    lst.append(ele)
    if i%2==0:
        even+=1
    else:
        odd+=1    

print(lst) 
print("number of even numbers",even)
print("number of odd numbers",odd)   